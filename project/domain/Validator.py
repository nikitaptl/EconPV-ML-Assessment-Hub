class Response:
    def __init__(self, is_succesful: bool, message):
        self.is_succesful = is_succesful
        self.message = message


class Validator:
    @staticmethod
    def is_float(str):
        try:
            float(str)
            return True
        except ValueError:
            return False

    @staticmethod
    def ValidatePvoutPrediction(DNI, DIF, TEMP)-> Response:
        if (not Validator.is_float(DNI)):
            return Response(False, "Вы ввели некорректный DNI")
        if(float(DNI) <= 0):
            return Response(False, "Вы ввели некорректный DNI: оно не может быть <= 0")
        if (not Validator.is_float(DIF)):
            return Response(False, "Вы ввели некорректный DIF")
        if(float(DIF) <= 0):
            return Response(False, "Вы ввели некорректный DIF: оно не может быть <= 0")
        if (not Validator.is_float(TEMP)):
            return Response(False, "Вы ввели некорректную температуру")
        return Response(True, [float(DNI), float(DIF), float(TEMP)])

    @staticmethod
    def ValidateNPVPrediction(energy_price, pvout, energy_consumption)-> Response:
        if (not Validator.is_float(energy_price)):
            return Response(False, "Вы ввели некорректную цену энергии")
        if(float(energy_price) <= 0):
            return Response(False, "Вы ввели некорректную цену энергии: она не может быть <= 0")
        if (not Validator.is_float(pvout)):
            return Response(False, "Вы ввели некорректный PVOUT")
        if(float(pvout) <= 0):
            return Response(False, "Вы ввели некорректный PVOUT: он не может быть <= 0")
        if (not Validator.is_float(energy_consumption)):
            return Response(False, "Вы ввели некорректный расход энергии в месяц")
        if(float(energy_consumption) <= 0):
            return Response(False, "Вы ввели некорректный расход энергии в месяц: он не может быть <= 0")
        return Response(True, [float(energy_price), float(pvout), float(energy_consumption)])
