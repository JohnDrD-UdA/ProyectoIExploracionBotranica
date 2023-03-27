from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plant(db.Model):
    __tablename__ = "Plant_Info"
    id = db.Column(db.Integer, primary_key=True)
    common_name = db.Column(db.String, nullable=False)
    scientific_name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    height = db.Column(db.Integer)
    isPousonous = db.Column(db.Boolean)
    isEatable = db.Column(db.Boolean)
    hasFlowers = db.Column(db.Boolean)
    produceFruits = db.Column(db.Boolean)
    isShadePlant = db.Column(db.Boolean)
    isSunPlant = db.Column(db.Boolean)
    image_Repositories = db.relationship('image_Repository', backref='plant')

class image_Repository(db.Model):
    __tablename__ = "image_Repository"
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('Plant_Info.id'))
