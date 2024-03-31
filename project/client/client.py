from project.training.train_modelPvout import ModelPvoutTrainer
from project.training.train_modelNPV import ModelNPVTrainer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import openpyxl
import joblib
import numpy as np

trainer = ModelNPVTrainer()
model = trainer.load_model()

new_data = pd.DataFrame({'Energy price': [3.8], 'PVOUT': [3.47], 'Energy consumption': [205]})

predictions = model.predict(new_data)
print("Предсказанные значения NPV:", predictions)

# trainer = ModelPvoutTrainer()
# model = trainer.model
#
# # Создание DataFrame с новыми значениями DNI, DIF и TEMP
# new_data = pd.DataFrame({'DNI': [3.764], 'DIF': [1.71], 'TEMP': [3.78]})
#
# # Сделать предсказания для новых значений
# predictions = model.predict(new_data)
#
# # Вывести предсказанные значения PVOUT
# print("Предсказанные значения PVOUT:", predictions)