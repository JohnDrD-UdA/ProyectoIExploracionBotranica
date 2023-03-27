from flask import Flask
from models import db
from routes import plant_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(plant_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()

