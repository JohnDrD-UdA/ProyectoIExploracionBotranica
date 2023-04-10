from fastapi import APIRouter
from schema.plantsSchema import plant
from config.db import conn
from models.models import Plants
from service.PlantService import PlantService
from typing import List

plantController= APIRouter()
service= PlantService()

@plantController.get("/plants")
def getPlants():
    result= service.getAllPlants()
    return result

@plantController.post("/plants/create")
def createPlant(data: plant):
    new_plant= data.dict()
    conn.execute(Plants.insert().values(new_plant))
    return "ok"

@plantController.get("/plants/{id}",response_model=plant)
def getPlantByID(id:int):
    result= service.getPlantByID(id)._asdict()
    return result

@plantController.get("/plnats/{name}",response_model=List[plant])
def getPlantsByName(name:str):
    result= service.getPlantByName(name)
    return result