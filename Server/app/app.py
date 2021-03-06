import os
import platform
import flask_restless
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from flask_cors import CORS

database_path = os.path.join(os.getcwd(), '..', 'database', 'database.db')
sqlite_prefix = 'sqlite:////'
if platform.system().lower() == 'windows':
    sqlite_prefix = sqlite_prefix[:-1]

app = Flask(__name__, template_folder="../static", static_folder='../static/dist')
app.config['SQLALCHEMY_DATABASE_URI'] = sqlite_prefix + database_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)


class PotionIngredient(db.Model):
    __tablename__ = 'PotionIngredients'

    id = Column(Integer, primary_key=True)
    ingredient_id = Column('IngredientId', Integer, ForeignKey('Ingredients.id'))
    ingredient = relationship('Ingredient', uselist=False)
    potion_id = Column('PotionId', Integer, ForeignKey('Potions.id'))
    potion = relationship('Potion', uselist=False)
    ingredients_per_potion = Column('IngredientsPerPotion', Integer, default=1)

    def __init__(self, ingredient, potion, ingredients_per_potion=1):
        self.ingredient = ingredient
        self.potion = potion
        self.ingredients_per_potion = ingredients_per_potion


class Ingredient(db.Model):
    __tablename__ = 'Ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    xp_reward = Column(Float)
    potion_ingredients = relationship('PotionIngredient', backref='Ingredient')
    ingredient_type_id = Column('IngredientTypeId', Integer, ForeignKey('IngredientTypes.id'))

    ingredient_type = relationship('IngredientType')

    def __init__(self, name, ingredient_type, xp_reward=None):
        self.name = name
        self.ingredient_type = ingredient_type
        self.xp_reward = xp_reward


class IngredientType(db.Model):
    __tablename__ = 'IngredientTypes'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    def __init__(self, name):
        self.name = name


class Potion(db.Model):
    __tablename__ = 'Potions'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    xp_reward = Column('XpReward', Float)
    potion_ingredients = relationship('PotionIngredient', backref='Potion')

    def __init__(self, name, xp_reward):
        self.name = name
        self.xp_reward = xp_reward


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/hello")
def hello():
    return "Hello World"


manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)
ingredient_blueprint = manager.create_api(Ingredient, methods=['GET'], max_results_per_page=-1, results_per_page=-1)
potion_blueprint = manager.create_api(Potion, methods=['GET'], max_results_per_page=-1, results_per_page=-1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)