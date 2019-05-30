from CarFactory import CarFactory
from helpers import creation_distance_min, creation_temps
import random

class Orchestrator:

    def __init__(self, x_min, x_max, n):
        self._x_min = x_min
        self._x_max = x_max
        self._n = n
        self._temps = creation_temps(x_min, x_max, n)

    def simulation(self, position_init, function, nombre_voitures):
        car_factory = CarFactory()
        leader = car_factory.create_leader(self._temps, position_init, function)
        cars = [leader]
        p = random.randint(2,6)
        for i in range(0, nombre_voitures):
            if i<=23:
                position_init = max(0, min(800 - p*i - creation_distance_min(25),800 - p * (i+1)))
                car = car_factory.create_car(self._temps, cars[i], 1, position_init)
            elif 24<=i<=60:
                position_init = max(0, min(800 - (p+5)*i - creation_distance_min(25),800 - (p+5) * (i+1)))
                car = car_factory.create_car(self._temps, cars[i], 1, position_init)
            else:
                position_init = 0
                car = car_factory.create_car(self._temps, cars[i], 1, position_init)
            cars.append(car)
        return cars

    
    @property
    def temps(self):
        return self._temps