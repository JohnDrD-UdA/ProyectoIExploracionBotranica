from flask import Blueprint, render_template
from models import Plant

plant_bp = Blueprint('plant', __name__)

@plant_bp.route('/')
def index():
    return 'Hello, world!'

@plant_bp.route('/plants')
def plants():
    all_plants = Plant.query.all()
    return render_template('plants.html', plants=all_plants)

@plant_bp.route('/add_plant', methods=['GET', 'POST'])
def add_plant():
    if request.method == 'POST':
        new_plant = Plant(common_name=request.form['common_name'],
                          scientific_name=request.form['scientific_name'],
                          description=request.form['description'])
        db.session.add(new_plant)
        db.session.commit()
        return redirect('/plants')
    else:
        return render_template('add_plant.html')
