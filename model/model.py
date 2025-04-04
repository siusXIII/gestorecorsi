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

    @staticmethod
    def getCorsiPDwithIscritti(pd):
        return DAO.getCorsiPDwithIscritti(pd)

    @staticmethod
    def getStudentiCorso(codins):
        studenti =  DAO.getStudentiCorso(codins)
        studenti.sort(key=lambda s: s.cognome)
        return studenti

    @staticmethod
    def getCDSofCorso(codins):
        cds = DAO.getCDSofCorso(codins)
        cds.sort(key=lambda c: c[1], reverse=True)
        return cds