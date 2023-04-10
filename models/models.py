from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String,Boolean
from config.db import engine,meta_data

Plants= Table("Plant_Info", meta_data, 
              Column("id",Integer, primary_key=True),
              Column("common_name",String(255), nullable=False),
              Column("scientific_name",String(255), nullable=False),
              Column("description",String(255), nullable=False),
              Column("height",Integer, nullable=False),
              Column("isPousonous",Boolean),
              Column("isEatable",Boolean),
              Column("hasFlowers",Boolean),
              Column("produceFruits",Boolean),
              Column("isShadePlant",Boolean),
              Column("isSunPlant",Boolean))

image_Repository= Table("image_Repository", meta_data, 
              Column("id",Integer, primary_key=True),
              Column("url",String(255), nullable=False),
              Column("description",String(255), nullable=False),
              Column("plant_id", Integer))

meta_data.create_all(engine)