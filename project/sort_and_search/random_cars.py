import random
import string
from application.entities.entities import Masina


# =========== Example of car brands, models and price ranges ==========================================================

car_details = {'BMW': {'models': ['3', '5', 'X3'],
                       'price-range': (40000, 80000)},
               'Audi': {'models': ['A4', 'Q5', 'A6'],
                        'price-range': (35000, 85000)},
               'Volvo': {'models': ['XC60', 'XC90', 'S60'],
                         'price-range': (40000, 90000)},
               'Acura': {'models': ['ILX', 'TLX', 'RDX'],
                         'price-range': (30000, 60000)},
               'Honda': {'models': ['Civic', 'Accord', 'CR-V'],
                         'price-range': (25000, 40000)},
               'Tesla': {'models': ['S', '3', 'X'],
                         'price-range': (40000, 90000)},
               'Nissan': {'models': ['Altima', 'Rogue', 'Pathfinder'],
                          'price-range': (25000, 45000)},
               'Volkswagen': {'models': ['Jetta', 'Golf', 'Tiguan'],
                              'price-range': (20000, 40000)},
               'Kia': {'models': ['Optima', 'Sorento', 'Sportage'],
                       'price-range': (20000, 40000)},
               'Mazda': {'models': ['3', '6', 'CX-5'],
                         'price-range': (20000, 35000)},
               'Lexus': {'models': ['ES', 'RX', 'NX'],
                         'price-range': (40000, 70000)},
               'Porsche': {'models': ['911', 'Cayenne', 'Macan'],
                           'price-range': (60000, 150000)},
               'Jeep': {'models': ['Wrangler', 'Cherokee', 'Renegade'],
                        'price-range': (30000, 60000)},
               }


# ========== Function that creates a random car object ================================================================

def create_car(details):
    # Random brand
    brand = random.choice(list(details.keys()))
    # Random model
    model = random.choice(list(details[brand]['models']))
    # Random token
    characters = string.ascii_lowercase + string.digits
    token = ''.join(random.choice(characters) for _ in range(10))
    # Random buy_price
    buy_price = random.randint(details[brand]['price-range'][0], details[brand]['price-range'][1])
    # Random sell_price
    sell_price = random.randint(int(buy_price/1.3), int(buy_price*1.3))

    # Create and return car entity
    random_car = Masina(brand, model, token, buy_price, sell_price)
    return random_car


# ========== Function that creates and writes 50000 random cars in a text file ========================================

def create_cars():
    with open('data/big_data', 'w') as f:
        for _ in range(50000):
            car = create_car(car_details)
            f.write(f"{car.marca} {car.model} {car.token_masina} {car.pret_achizitie} {car.pret_vanzare}\n")
