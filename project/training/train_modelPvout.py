import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
import os

class ModelPvoutTrainer:
    model = None
    path_input = None
    path_output = None

    def __init__(self, path_input="project/training/datasets/datasetModelPvout.xlsx",
                 path_output="project/training/saved_models/modelPvout.joblib"):
        self.path_input = path_input
        self.path_output = path_output

    def train(self):
        data = pd.read_excel(self.path_input)

        X = data.drop(columns=['PVOUT']).drop(columns=['Region'])
        y = data['PVOUT']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(X_train, y_train)

        # Оценка качества модели
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print("Среднеквадратичная ошибка (MSE):", mse)

        self.model = model
        self.save_model()

    def save_model(self):
        if (self.model == None):
            return "You have not created model yet!"
        joblib.dump(self.model, self.path_output)

    def load_model(self):
        if (not os.path.exists(self.path_output)):
            print("You have not created model yet!")
        return joblib.load(self.path_output)
