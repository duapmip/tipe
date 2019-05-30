from CarFactory import CarFactory
from helpers import creation_distance_min, creation_temps
import random

class Orchestrator:

    def __init__(self):
        pass

    def simulation(self, x_min, x_max, n, position_init, function, nombre_voitures):
        temps = creation_temps(x_min, x_max, n)
        car_factory = CarFactory()
        leader = car_factory.create_leader(temps, position_init, function)
        cars = [leader]
        p = random.randint(2,6)
        for i in range(0, nombre_voitures):
            if i<=23:
                position_init = max(0, min(800 - p*i - creation_distance_min(25),800 - p * (i+1)))
                car = car_factory.create_car(temps, cars[i], 1, position_init)
            elif 24<=i<=60:
                position_init = max(0, min(800 - (p+5)*i - creation_distance_min(25),800 - (p+5) * (i+1)))
                car = car_factory.create_car(temps, cars[i], 1, position_init)
            else:
                position_init = 0
                car = car_factory.create_car(temps, cars[i], 1, position_init)
            cars.append(car)
        return cars

    
    