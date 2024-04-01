import sklearn.base

from project.training.train_modelNPV import ModelNPVTrainer
from project.training.train_modelPvout import ModelPvoutTrainer
from project.training.train_modelKWP import ModelKWPTrainer
from project.domain.Validator import Response, Validator
import os
import joblib
import pandas as pd


class Predictor:
    trainerPvout = None
    trainerNPV = None
    trainerKWP = None
    modelPvout = None
    modelNPV = None
    modelKWP = None

    def __init__(self, path_datasetPvout="project/training/datasets/datasetModelPvout.xlsx",
                 path_datasetNPV="project/training/datasets/datasetModelNPV.xlsx",
                 path_modelPvout="project/training/saved_models/modelPvout.joblib",
                 path_modelNPV="project/training/saved_models/modelNPV.joblib",
                 path_modelKWP="project/training/saved_models/modelKWP.joblib"):
        self.trainerPvout = ModelPvoutTrainer(path_datasetPvout, path_modelPvout)
        self.trainerNPV = ModelNPVTrainer(path_datasetNPV, path_modelNPV)
        self.trainerKWP = ModelKWPTrainer(path_datasetNPV, path_modelKWP)

        if (os.path.exists(path_modelPvout)):
            self.modelPvout = joblib.load(path_modelPvout)
        else:
            self.trainerPvout.train()
            self.modelPvout = self.trainerPvout.load_model()

        if (os.path.exists(path_modelNPV)):
            self.modelNPV = joblib.load(path_modelNPV)
        else:
            self.trainerNPV.train()
            self.modelNPV = self.trainerNPV.load_model()

        if (os.path.exists(path_modelKWP)):
            self.modelKWP = joblib.load(path_modelKWP)
        else:
            self.trainerKWP.train()
            self.modelKWP = self.trainerKWP.load_model()

    def predictPvout(self, DNI, DIF, TEMP):
        response = Validator.ValidatePvoutPrediction(DNI, DIF, TEMP)
        if (not response.is_succesful):
            return response

        data_forecast = pd.DataFrame(
            {'DNI': [response.message[0]], 'DIF': [response.message[1]], 'TEMP': [response.message[2]]})
        result = self.modelPvout.predict(data_forecast)

        return Response(True, result[0])

    def predictNPV(self, energy_price, pvout, energy_consumption):
        response = Validator.ValidateNPVPrediction(energy_price, pvout, energy_consumption)
        if (not response.is_succesful):
            return response

        data_forecast = pd.DataFrame(
            {'Energy price': [response.message[0]], 'PVOUT': [response.message[1]],
             'Energy consumption': [response.message[2]]})
        result = self.modelNPV.predict(data_forecast)

        return Response(True, result[0])

    def predictKWP(self, energy_price, pvout, energy_consumption):
        response = Validator.ValidateNPVPrediction(energy_price, pvout, energy_consumption)
        if (not response.is_succesful):
            return response

        data_forecast = pd.DataFrame(
            {'Energy price': [response.message[0]], 'PVOUT': [response.message[1]],
             'Energy consumption': [response.message[2]]})
        result = self.modelKWP.predict(data_forecast)

        return Response(True, result[0])
