from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import joblib
import pandas
import os


class ModelKWPTrainer:
    temp = 1.075  # Темпы роста цен на электроэнергию
    infl = 1.09  # Инфляция
    pv_cost = 50000  # Стоимость kWp солнечной электростанции
    model = None
    path_input = None
    path_output = None

    def __init__(self, path_input="project/training/datasets/datasetModelNPV.xlsx",
                 path_output="project/training/saved_models/modelKWP.joblib"):
        self.path_input = path_input
        self.path_output = path_output

    # Создание Techno-economic optimization model
    def createTEOM(self):
        column_names = ['Energy price', 'PVOUT', 'Energy consumption']
        data = pandas.read_excel(self.path_input, header=None, skiprows=1, names=column_names)
        data['n'] = float(0)

        # Здесь для каждого семпла находится максимально возможное NPV для него
        # и оптимальная мощность батареи
        for index, row in data.iterrows():
            costElectr = row['Energy price']
            demand = row['Energy consumption']
            pvout = row['PVOUT']

            npv = float('-inf')
            opt_n = float('-inf')
            for n in [0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.25, 4.5, 4.75, 5, 5.25,
                      5.5, 5.75, 6]:
                res = -self.pv_cost * n
                for j in range(1, 20):
                    Ci = (self.temp ** j) * demand * 12 * costElectr
                    Ri = n * pvout * 365 * costElectr
                    profit = min(Ci, Ri) / (self.infl ** j)
                    res += profit
                if res > npv:
                    npv = res
                    opt_n = n

            if npv <= 0:
                data.at[index, 'n'] = 0
            else:
                data.at[index, 'n'] = opt_n

        data.to_excel('project/training/datasets/outputKWP.xlsx', index=False)
        return data

    def train(self):
        data = self.createTEOM()

        # Признаки - стоимость электроэнергии, производительность батареи, средняя трата электроэнергии
        X = data[['Energy price', 'PVOUT', 'Energy consumption']]
        # Целевая переменная - n
        y = data['n']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Создание модели случайного леса
        rf_model = RandomForestRegressor(random_state=42)
        param_grid = {
            'n_estimators': [50, 100, 150, 200],
            'max_depth': [None, 10, 20, 30, 40],
            'min_samples_split': [2, 5, 10, 15],
            'min_samples_leaf': [1, 2, 4, 8]
        }

        # Кросс-валидация
        grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error',
                                   n_jobs=-1)
        grid_search.fit(X_train, y_train)
        best_params = grid_search.best_params_

        # Обучение модели
        best_rf_model = RandomForestRegressor(**best_params, random_state=42)
        best_rf_model.fit(X_train, y_train)

        # Оценка производительности модели
        predictions = best_rf_model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print('\nMean Squared Error на тестовом наборе данных:', mse)
        self.model = best_rf_model
        self.save_model()

    def save_model(self):
        if (self.model == None):
            print("You have not created model yet!")
        joblib.dump(self.model, self.path_output)

    def load_model(self):
        if (not os.path.exists(self.path_output)):
            print("You have not created model yet!")
        return joblib.load(self.path_output)
