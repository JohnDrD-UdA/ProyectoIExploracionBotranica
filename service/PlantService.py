from Iservice.IPlantsService import IPlantService
from sqlalchemy import or_
from config.db import conn
from models.models import Plants

class PlantService(IPlantService):

    
    def getAllPlants(self):
        result=conn.execute(Plants.select())
        resultAsList=[r._asdict() for r in result]
        return resultAsList
    
    def getPlantByID(self,id:int):
        return conn.execute(Plants.select().where(Plants.c.id== id)).first()
    
    def getPlantByName(self,name:str):
        resultRaw=conn.execute(Plants.select().where(or_(Plants.c.common_name.contains(name),Plants.c.scientific_name.contains(name) )))
        result=[r._asdict() for r in resultRaw]
        return result