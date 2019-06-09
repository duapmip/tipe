""""Simulator.py"""

from src.CarFactory import CarFactory
from src.helpers import creation_distance_min, creation_temps
import random


class Simulator:
    """Classe permettant d effectuer la simulation et d obtenir toute les voitures.

    Attributs:
        x_min (int): debut de la simulation
        x_max (int): Fin de la simulation
        n (int): Pas de la simulation
    """

    def __init__(self, x_min, x_max, n):
        self._x_min = x_min
        self._x_max = x_max
        self._n = n
        self._temps = creation_temps(x_min, x_max, n)

    def simulation(self, nombre_voitures, position_init, vitesse_init, leader_function, simulator_function, model):
        """Creation des voitures

        Args: 
            nombre_voitures (int) Nombre de voitures
            position_init (int): position initiale
            vitesse_init (int):vitesse intiiale
            leader_function (function): Fonction du leader
            simulator_function (function):Fonction de simulation
            model (str): Modele

        Returns:
            list: Liste de voitures
        """
        car_factory = CarFactory()
        leader = car_factory.create_leader(self._temps, position_init, vitesse_init, leader_function)
        cars = [leader]
        p = random.randint(4,8)
        for i in range(0, nombre_voitures):
            car = simulator_function(i, p, vitesse_init, position_init, car_factory, cars, self._temps, model)
            cars.append(car)
        return cars

    
    @property
    def temps(self):
        return self._temps