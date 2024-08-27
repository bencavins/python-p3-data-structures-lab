spicy_foods = [
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
    result = []
    for food in spicy_foods:
        result.append(food['name'])
    return result

def get_spiciest_foods(spicy_foods):
    spiciest = []
    for food in spicy_foods:
        if food['heat_level'] > 5:
            spiciest.append(food)
    return spiciest

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        heat_emoji = '🌶' * heat_level
        print(f'{name} ({cuisine}) | Heat Level: {heat_emoji}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass


# print(get_names(spicy_foods))
