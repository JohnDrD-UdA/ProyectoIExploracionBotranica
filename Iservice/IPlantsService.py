from abc import ABCMeta,abstractclassmethod

class IPlantService(metaclass=ABCMeta):
    @abstractclassmethod
    def getAllPlants(self):
        pass
    @abstractclassmethod
    def getPlantByID(self,id:int):
        pass
    @abstractclassmethod
    def getPlantByName(self,name:str):
        pass