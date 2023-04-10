from fastapi import FastAPI
from controller.plantController import plantController	
app= FastAPI()

app.include_router(plantController)