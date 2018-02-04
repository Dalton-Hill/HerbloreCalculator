import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    ingredient_types = {
        'herb': app.IngredientType("Herb"),
        'potion': app.IngredientType("Potion"),
        'secondary': app.IngredientType("Secondary")
    }

    ingredients = {
        'clean_guam': app.Ingredient(name='Clean Guam', ingredient_type=ingredient_types['herb']),
        'clean_marrentill': app.Ingredient(name='Clean Marrentill', ingredient_type=ingredient_types['herb']),
        'clean_tarromin': app.Ingredient(name='Clean Tarromin', ingredient_type=ingredient_types['herb']),
        'eye_of_newt': app.Ingredient(name='Eye of Newt', ingredient_type=ingredient_types['secondary']),
        'unicorn_horn_dust': app.Ingredient(name='Unicorn Horn Dust', ingredient_type=ingredient_types['secondary']),
        'limpwurt_root': app.Ingredient(name='Limpwurt Root', ingredient_type=ingredient_types['secondary']),
        'amylase_crystal': app.Ingredient(name='Amylase Crystal', ingredient_type=ingredient_types['secondary']),
        'super_energy': app.Ingredient(name='Super Energy (4)', ingredient_type=ingredient_types['secondary']),
    }

    potions = {
        'attack_potion':  app.Potion(name='Attack Potion (3)', xp_reward=25),
        'antipoison':  app.Potion(name='Antipoison (3)', xp_reward=37.5),
        'strength_potion':  app.Potion(name='Strength Potion (3)', xp_reward=50),
        'stamina_potion':  app.Potion(name='Stamina Potion (4)', xp_reward=102),
    }

    potion_ingredients = {
         app.PotionIngredient(ingredients['clean_guam'], potions['attack_potion']),
         app.PotionIngredient(ingredients['eye_of_newt'], potions['attack_potion']),
         app.PotionIngredient(ingredients['clean_marrentill'], potions['antipoison']),
         app.PotionIngredient(ingredients['unicorn_horn_dust'], potions['antipoison']),
         app.PotionIngredient(ingredients['clean_tarromin'], potions['strength_potion']),
         app.PotionIngredient(ingredients['limpwurt_root'], potions['strength_potion']),
         app.PotionIngredient(ingredients['amylase_crystal'], potions['stamina_potion'], ingredients_per_potion=4),
         app.PotionIngredient(ingredients['super_energy'], potions['stamina_potion']),
    }

    engine = create_engine(app.sqlite_prefix + app.database_path)
    Session = sessionmaker(bind=engine)
    session = Session()

    app.db.create_all()

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