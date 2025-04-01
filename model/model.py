from database.DAO import DAO


class Model:
    def __init__(self):
        pass
    @staticmethod
    def getCodins():
        return DAO.getCodins()
    @staticmethod
    def getAllCorsi():
        return DAO.getAllCorsi()
    @staticmethod
    def getCorsiPD(pd):
        return DAO.getCorsiPD(pd)