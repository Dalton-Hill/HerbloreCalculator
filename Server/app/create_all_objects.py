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
        'clean_guam_leaf': app.Ingredient(name='Clean Guam leaf', ingredient_type=ingredient_types['herb']),
        'clean_marrentill': app.Ingredient(name='Clean Marrentill', ingredient_type=ingredient_types['herb']),
        'clean_tarromin': app.Ingredient(name='Clean Tarromin', ingredient_type=ingredient_types['herb']),
        'clean_harralander': app.Ingredient(name='Clean Harralander', ingredient_type=ingredient_types['herb']),
        'clean_ranarr_weed': app.Ingredient(name='Clean Ranarr weed', ingredient_type=ingredient_types['herb']),
        'clean_toadflax': app.Ingredient(name='Clean Toadflax', ingredient_type=ingredient_types['herb']),
        'clean_irit_leaf': app.Ingredient(name='Clean Irit leaf', ingredient_type=ingredient_types['herb']),
        'clean_avantoe': app.Ingredient(name='Clean Avantoe', ingredient_type=ingredient_types['herb']),
        'clean_kwuarm': app.Ingredient(name='Clean Kwuarm', ingredient_type=ingredient_types['herb']),
        'clean_snapdragon': app.Ingredient(name='Clean Snapdragon', ingredient_type=ingredient_types['herb']),
        'clean_cadantine': app.Ingredient(name='Clean Cadantine', ingredient_type=ingredient_types['herb']),
        'clean_lantadyme': app.Ingredient(name='Clean Lantadyme', ingredient_type=ingredient_types['herb']),
        'clean_dwarf_weed': app.Ingredient(name='Clean Dwarf weed', ingredient_type=ingredient_types['herb']),
        'clean_torstol': app.Ingredient(name='Clean Torstol', ingredient_type=ingredient_types['herb']),

        'swamp_tar': app.Ingredient(name='Swamp tar', ingredient_type=ingredient_types['secondary']),
        'volcanic_ash': app.Ingredient(name='Volcanic ash', ingredient_type=ingredient_types['secondary']),
        'ashes': app.Ingredient(name='Ashes', ingredient_type=ingredient_types['secondary']),
        'white_berries': app.Ingredient(name='White berries', ingredient_type=ingredient_types['secondary']),
        'snape_grass': app.Ingredient(name='Snape grass', ingredient_type=ingredient_types['secondary']),
        'toads_legs': app.Ingredient(name='Toad\'s legs', ingredient_type=ingredient_types['secondary']),
        'chocolate_dust': app.Ingredient(name='Chocolate dust', ingredient_type=ingredient_types['secondary']),
        'goat_horn_dust': app.Ingredient(name='Goat horn dust', ingredient_type=ingredient_types['secondary']),
        'eye_of_newt': app.Ingredient(name='Eye of Newt', ingredient_type=ingredient_types['secondary']),
        'unicorn_horn_dust': app.Ingredient(name='Unicorn horn dust', ingredient_type=ingredient_types['secondary']),
        'limpwurt_root': app.Ingredient(name='Limpwurt Root', ingredient_type=ingredient_types['secondary']),
        'amylase_crystal': app.Ingredient(name='Amylase Crystal', ingredient_type=ingredient_types['secondary']),
        'yew_roots': app.Ingredient(name='Yew Roots', ingredient_type=ingredient_types['secondary']),
        'crushed_birds_nest': app.Ingredient(name='Crushed bird\'s nest',
                                             ingredient_type=ingredient_types['secondary']),
        'coconut_milk': app.Ingredient(name='Coconut milk', ingredient_type=ingredient_types['secondary']),
        'magic_roots': app.Ingredient(name='Magic roots', ingredient_type=ingredient_types['secondary']),
        'mort_myre_fungi': app.Ingredient(name='Mort myre fungi', ingredient_type=ingredient_types['secondary']),
        'kebbit_teeth_dust': app.Ingredient(name='Kebbit teeth dust', ingredient_type=ingredient_types['secondary']),
        'dragon_scale_dust': app.Ingredient(name='Dragon scale dust', ingredient_type=ingredient_types['secondary']),
        'red_spiders_eggs': app.Ingredient(name='Red spiders\' eggs', ingredient_type=ingredient_types['secondary']),
        'potatoe_cactus': app.Ingredient(name='Potato cactus', ingredient_type=ingredient_types['secondary']),
        'wine_of_zamorak': app.Ingredient(name='Wine of Zamorak', ingredient_type=ingredient_types['secondary']),
        'jangerberries': app.Ingredient(name='Jangerberries', ingredient_type=ingredient_types['secondary']),

        'super_energy': app.Ingredient(name='Super Energy (4)', ingredient_type=ingredient_types['potion']),
        'super_attack': app.Ingredient(name='Super attack (4)', ingredient_type=ingredient_types['potion']),
        'super_strength': app.Ingredient(name='Super strength (4)', ingredient_type=ingredient_types['potion']),
        'super_defence': app.Ingredient(name='Super defence (4)', ingredient_type=ingredient_types['potion']),
        'anti_venom': app.Ingredient(name='Anti-venom (3)', ingredient_type=ingredient_types['potion']),
    }

    potions = {
        'attack_potion':  app.Potion(name='Attack Potion (3)', xp_reward=25),
        'guam_tar':  app.Potion(name='Guam tar (15)', xp_reward=30),
        'antipoison':  app.Potion(name='Antipoison (3)', xp_reward=37.5),
        'guthix_rest':  app.Potion(name='Guthix rest', xp_reward=59.5),
        'marrentill_tar': app.Potion(name='Marrentill tar (15)', xp_reward=42.5),
        'strength_potion':  app.Potion(name='Strength Potion (3)', xp_reward=50),
        'serum_207':  app.Potion(name='Serum 207 (3)', xp_reward=50),
        'tarromin_tar': app.Potion(name='Tarromin tar (15)', xp_reward=55),
        'compost_potion': app.Potion(name='Compost Potion (3)', xp_reward=60),
        'energy_potion': app.Potion(name='Energy Potion (3)', xp_reward=67.5),
        'combat_potion': app.Potion(name='Combat Potion (3)', xp_reward=84),
        'harralander_tar': app.Potion(name='Harralander tar (15)', xp_reward=72.5),
        'defence_potion': app.Potion(name='Defence Potion (3)', xp_reward=75),
        'prayer_potion': app.Potion(name='Prayer Potion (3)', xp_reward=87.5),
        'agility_potion': app.Potion(name='Agility Potion (3)', xp_reward=80),
        'antidote_plus': app.Potion(name='Antidote+ (3)', xp_reward=80),
        'saradomin_brew': app.Potion(name='Saradomin brew (3)', xp_reward=180),
        'super_attack': app.Potion(name='Super attack (3)', xp_reward=100),
        'super_antipoison': app.Potion(name='Super antipoison (3)', xp_reward=106.3),
        'antidote_plus_plus': app.Potion(name='Antidote++ (3)', xp_reward=177.5),
        'fishing_potion': app.Potion(name='Fishing potion (3)', xp_reward=112.5),
        'super_energy_potion': app.Potion(name='Super energy potion (3)', xp_reward=117.5),
        'hunter_potion': app.Potion(name='Hunter potion (3)', xp_reward=120),
        'super_strength': app.Potion(name='Super strength (3)', xp_reward=125),
        'weapon_poison': app.Potion(name='Weapon poison (3)', xp_reward=137.5),
        'super_restore': app.Potion(name='Super restore (3)', xp_reward=142.5),
        'super_defence': app.Potion(name='Super defence (3)', xp_reward=150),
        'antifire_potion': app.Potion(name='Antifire potion (3)', xp_reward=157.5),
        'magic_potion': app.Potion(name='Magic potion (3)', xp_reward=172.5),
        'ranging_potion': app.Potion(name='Ranging potion (3)', xp_reward=162.5),
        'zamorak_brew': app.Potion(name='Zamorak brew (3)', xp_reward=175),
        'super_combat_potion': app.Potion(name='Super combat potion (4)', xp_reward=150),
        'anti_venom_plus': app.Potion(name='Anti-venom+ (3)', xp_reward=125),
        'stamina_potion':  app.Potion(name='Stamina Potion (4)', xp_reward=102),
    }

    potion_ingredients = {
         app.PotionIngredient(ingredients['clean_guam_leaf'], potions['attack_potion']),
         app.PotionIngredient(ingredients['eye_of_newt'], potions['attack_potion']),

         app.PotionIngredient(ingredients['clean_guam_leaf'], potions['guam_tar']),
         app.PotionIngredient(ingredients['swamp_tar'], potions['guam_tar'], ingredients_per_potion=15),

         app.PotionIngredient(ingredients['clean_marrentill'], potions['antipoison']),
         app.PotionIngredient(ingredients['unicorn_horn_dust'], potions['antipoison']),

         app.PotionIngredient(ingredients['clean_marrentill'], potions['guthix_rest']),
         app.PotionIngredient(ingredients['clean_harralander'], potions['guthix_rest']),

         app.PotionIngredient(ingredients['clean_marrentill'], potions['marrentill_tar']),
         app.PotionIngredient(ingredients['swamp_tar'], potions['marrentill_tar'], ingredients_per_potion=15),

         app.PotionIngredient(ingredients['clean_tarromin'], potions['strength_potion']),
         app.PotionIngredient(ingredients['limpwurt_root'], potions['strength_potion']),

         app.PotionIngredient(ingredients['clean_tarromin'], potions['serum_207']),
         app.PotionIngredient(ingredients['ashes'], potions['serum_207']),

         app.PotionIngredient(ingredients['clean_tarromin'], potions['tarromin_tar']),
         app.PotionIngredient(ingredients['swamp_tar'], potions['tarromin_tar'], ingredients_per_potion=15),

         app.PotionIngredient(ingredients['clean_harralander'], potions['compost_potion']),
         app.PotionIngredient(ingredients['volcanic_ash'], potions['compost_potion']),

         app.PotionIngredient(ingredients['clean_harralander'], potions['energy_potion']),
         app.PotionIngredient(ingredients['chocolate_dust'], potions['energy_potion']),

         app.PotionIngredient(ingredients['clean_harralander'], potions['combat_potion']),
         app.PotionIngredient(ingredients['goat_horn_dust'], potions['combat_potion']),

         app.PotionIngredient(ingredients['clean_harralander'], potions['harralander_tar']),
         app.PotionIngredient(ingredients['swamp_tar'], potions['harralander_tar'], ingredients_per_potion=15),

         app.PotionIngredient(ingredients['clean_ranarr_weed'], potions['defence_potion']),
         app.PotionIngredient(ingredients['white_berries'], potions['defence_potion']),

         app.PotionIngredient(ingredients['clean_ranarr_weed'], potions['prayer_potion']),
         app.PotionIngredient(ingredients['snape_grass'], potions['prayer_potion']),

         app.PotionIngredient(ingredients['clean_toadflax'], potions['agility_potion']),
         app.PotionIngredient(ingredients['toads_legs'], potions['agility_potion']),

         app.PotionIngredient(ingredients['clean_toadflax'], potions['antidote_plus']),
         app.PotionIngredient(ingredients['yew_roots'], potions['antidote_plus']),

         app.PotionIngredient(ingredients['clean_toadflax'], potions['saradomin_brew']),
         app.PotionIngredient(ingredients['crushed_birds_nest'], potions['saradomin_brew']),

         app.PotionIngredient(ingredients['clean_irit_leaf'], potions['super_attack']),
         app.PotionIngredient(ingredients['eye_of_newt'], potions['super_attack']),

         app.PotionIngredient(ingredients['clean_irit_leaf'], potions['super_antipoison']),
         app.PotionIngredient(ingredients['unicorn_horn_dust'], potions['super_antipoison']),

         app.PotionIngredient(ingredients['clean_irit_leaf'], potions['antidote_plus_plus']),
         app.PotionIngredient(ingredients['coconut_milk'], potions['antidote_plus_plus']),
         app.PotionIngredient(ingredients['magic_roots'], potions['antidote_plus_plus']),

         app.PotionIngredient(ingredients['clean_avantoe'], potions['fishing_potion']),
         app.PotionIngredient(ingredients['snape_grass'], potions['fishing_potion']),

         app.PotionIngredient(ingredients['clean_avantoe'], potions['super_energy_potion']),
         app.PotionIngredient(ingredients['mort_myre_fungi'], potions['super_energy_potion']),

         app.PotionIngredient(ingredients['clean_avantoe'], potions['hunter_potion']),
         app.PotionIngredient(ingredients['kebbit_teeth_dust'], potions['hunter_potion']),

         app.PotionIngredient(ingredients['clean_kwuarm'], potions['super_strength']),
         app.PotionIngredient(ingredients['limpwurt_root'], potions['super_strength']),

         app.PotionIngredient(ingredients['clean_kwuarm'], potions['weapon_poison']),
         app.PotionIngredient(ingredients['dragon_scale_dust'], potions['weapon_poison']),

         app.PotionIngredient(ingredients['clean_snapdragon'], potions['super_restore']),
         app.PotionIngredient(ingredients['red_spiders_eggs'], potions['super_restore']),

         app.PotionIngredient(ingredients['clean_cadantine'], potions['super_defence']),
         app.PotionIngredient(ingredients['white_berries'], potions['super_defence']),

         app.PotionIngredient(ingredients['clean_lantadyme'], potions['antifire_potion']),
         app.PotionIngredient(ingredients['dragon_scale_dust'], potions['antifire_potion']),

         app.PotionIngredient(ingredients['clean_lantadyme'], potions['magic_potion']),
         app.PotionIngredient(ingredients['potatoe_cactus'], potions['magic_potion']),

         app.PotionIngredient(ingredients['clean_dwarf_weed'], potions['ranging_potion']),
         app.PotionIngredient(ingredients['wine_of_zamorak'], potions['ranging_potion']),

         app.PotionIngredient(ingredients['clean_torstol'], potions['zamorak_brew']),
         app.PotionIngredient(ingredients['jangerberries'], potions['zamorak_brew']),

         app.PotionIngredient(ingredients['clean_torstol'], potions['super_combat_potion']),
         app.PotionIngredient(ingredients['super_attack'], potions['super_combat_potion']),
         app.PotionIngredient(ingredients['super_strength'], potions['super_combat_potion']),
         app.PotionIngredient(ingredients['super_defence'], potions['super_combat_potion']),

         app.PotionIngredient(ingredients['clean_torstol'], potions['anti_venom_plus']),
         app.PotionIngredient(ingredients['anti_venom'], potions['anti_venom_plus']),

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