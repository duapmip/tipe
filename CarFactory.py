from Car import Car
import random

class CarFactory:

    def __init__(self):
        pass

    
    def create_leader(self, temps, position_init, function):
        car = Car(temps)
        car.set_leader(position_init, function)
        return car


    def create_car(self, temps, leader, temps_init, position_init):
        car = Car(temps)
        vitesse_init = random.randint(12,16)
        vitesse_max = self._creation_vitesse_max(0.8, 25)
        car.set_caracteristiques(leader, temps_init, position_init, vitesse_init, vitesse_max)
        return car

    @staticmethod
    def _creation_vitesse_max(p, vitesse_max):
        if random.random() < p:
            return random.randint(-5,5) + vitesse_max
        return vitesse_max
