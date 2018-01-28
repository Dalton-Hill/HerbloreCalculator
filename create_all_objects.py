from server.HerbloreCalculator.secret import mysql_password
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from server.HerbloreCalculator.HerbloreCalculatorApp import Ingredient, IngredientType, Potion, db, PotionIngredient


if __name__ == '__main__':
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
        'unicorn_horn_dust': Ingredient(name='Unicorn Horn Dust', ingredient_type=ingredient_types['secondary']),
        'limpwurt_root': Ingredient(name='Limpwurt Root', ingredient_type=ingredient_types['secondary']),
        'amylase_crystal': Ingredient(name='Amylase Crystal', ingredient_type=ingredient_types['secondary']),
        'super_energy': Ingredient(name='Super Energy (4)', ingredient_type=ingredient_types['secondary']),
    }

    potions = {
        'attack_potion': Potion(name='Attack Potion (3)', xp_reward=25),
        'antipoison': Potion(name='Antipoison (3)', xp_reward=37.5),
        'strength_potion': Potion(name='Strength Potion (3)', xp_reward=50),
        'stamina_potion': Potion(name='Stamina Potion (4)', xp_reward=102),
    }

    potion_ingredients = {
        PotionIngredient(ingredients['clean_guam'], potions['attack_potion']),
        PotionIngredient(ingredients['eye_of_newt'], potions['attack_potion']),
        PotionIngredient(ingredients['clean_marrentill'], potions['antipoison']),
        PotionIngredient(ingredients['unicorn_horn_dust'], potions['antipoison']),
        PotionIngredient(ingredients['clean_tarromin'], potions['strength_potion']),
        PotionIngredient(ingredients['limpwurt_root'], potions['strength_potion']),
        PotionIngredient(ingredients['amylase_crystal'], potions['stamina_potion'], ingredients_per_potion=4),
        PotionIngredient(ingredients['super_energy'], potions['stamina_potion']),
    }

    engine = create_engine('mysql+mysqldb://root:{}@localhost/HerbloreCalculator'.format(mysql_password))
    Session = sessionmaker(bind=engine)
    session = Session()

    db.create_all()

    for ingredient_type in ingredient_types.values():
        session.add(ingredient_type)

    for ingredient in ingredients.values():
        session.add(ingredient)

    for potion in potions.values():
        session.add(potion)

    for potion_ingredient in potion_ingredients:
        session.add(potion_ingredient)

    session.commit()
    session.close()