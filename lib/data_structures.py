foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    pass

def get_spiciest_foods(spicy_foods):
    pass

def print_spicy_foods(spicy_foods):
    for food_dict in spicy_foods:
        peppers = food_dict['heat_level'] * '🌶'
        print(f"{food_dict['name']} ({food_dict['cuisine']}) | Heat Level: {peppers}")

print_spicy_foods(foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    total = 0
    for food_dict in spicy_foods:
        total += food_dict['heat_level']
    return total / len(spicy_foods)

get_average_heat_level(foods)

def create_spicy_food(spicy_foods, spicy_food):
    pass


