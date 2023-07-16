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
    return [x["name"] for x in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    return [x for x in spicy_foods if x["heat_level"] >= 5]
    pass

def print_spicy_foods(spicy_foods):
    for x in spicy_foods:
        print(f'{x["name"]} ({x["cuisine"]}) | Heat Level: {("🌶"*x["heat_level"])}')
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for x in spicy_foods:
        if x["cuisine"] == cuisine:
            return x
    pass

def print_spiciest_foods(spicy_foods):
    s = get_spiciest_foods(spicy_foods)
    print_spicy_foods(s)
    pass

def get_average_heat_level(spicy_foods):
    l = [x["heat_level"] for x in spicy_foods]
    return sum(l) // len(l)
    pass

def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods + [spicy_food]
    pass
