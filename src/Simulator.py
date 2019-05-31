from src.CarFactory import CarFactory
from src.helpers import creation_distance_min, creation_temps
import random

class Simulator:

    def __init__(self, x_min, x_max, n):
        self._x_min = x_min
        self._x_max = x_max
        self._n = n
        self._temps = creation_temps(x_min, x_max, n)

    def simulation(self, nombre_voitures, position_init, vitesse_init, leader_function, simulator_function, model):
        car_factory = CarFactory()
        leader = car_factory.create_leader(self._temps, position_init, vitesse_init, leader_function)
        cars = [leader]
        p = random.randint(2,6)
        for i in range(0, nombre_voitures):
            car = simulator_function(i, p, vitesse_init, position_init, car_factory, cars, self._temps, model)
            cars.append(car)
        return cars

    
    @property
    def temps(self):
        return self._temps