from HerbloreCalculator.secret import mysql_password
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from server.HerbloreCalculator.HerbloreCalculatorApp import Ingredient, IngredientType, Potion, db

ingredient_types = {
    'herb': IngredientType("Herb"),
    'potion': IngredientType("Potion"),
    'secondary': IngredientType("Secondary")
}


ingredients = {
    'clean_guam': Ingredient(name='Clean Guam', ingredient_type=ingredient_types['herb']),
    'clean_marrentill': Ingredient(name='Clean Marrentill', ingredient_type=ingredient_types['herb']),
    'clean_tarromin': Ingredient(name='Clean Tarromin', ingredient_type=ingredient_types['herb']),
    'eye_of_newt': Ingredient(name='Eye of Newt', ingredient_type=ingredient_types['secondary']),
    'unicorn_horn_dust': Ingredient(name='Clean Tarromin', ingredient_type=ingredient_types['secondary']),
    'limpwurt_root': Ingredient(name='Clean Tarromin', ingredient_type=ingredient_types['secondary']),
}


potions = {
    Potion(name='Attack Potion', xp_reward=25, ingredients=[ingredients['clean_guam'], ingredients['eye_of_newt']]),
    Potion(name='Antipoison', xp_reward=37.5, ingredients=[ingredients['clean_marrentill'],
                                                           ingredients['unicorn_horn_dust']]),
    Potion(name='Strength Potion', xp_reward=50, ingredients=[ingredients['clean_tarromin'],
                                                              ingredients['limpwurt_root']]),
}

engine = create_engine('mysql+mysqldb://root:{}@localhost/HerbloreCalculator'.format(mysql_password))
Session = sessionmaker(bind=engine)
session = Session()

db.create_all()

for ingredient_type in ingredient_types.values():
    session.add(ingredient_type)

for ingredient in ingredients.values():
    session.add(ingredient)

for potion in potions:
    session.add(potion)

session.commit()
session.close()