from src.CarPerso import CarPerso
from src.CarIDM import CarIDM
from src.CarLeader import CarLeader
import random

# Creation d'une classe permettant de creer et definir toutes les voitures 

class CarFactory:

    def __init__(self):
        pass

    
    def create_leader(self, temps, position_init, vitesse_init, function):
        leader = CarLeader(temps)
        leader.set_leader(position_init, vitesse_init, function)
        return leader


    def create_car(self, temps, leader, temps_init, position_init, model):
        if model == "perso":
            car = CarPerso(temps)
        elif model == "idm":
            car = CarIDM(temps)
        else:
            raise Exception("This model does not exist.")
        vitesse_init = random.randint(12,16)
        vitesse_max = self._creation_vitesse_max(0.8, 25)
        car.set_caracteristiques(leader, temps_init, position_init, vitesse_init, vitesse_max)
        return car

    @staticmethod
    def _creation_vitesse_max(p, vitesse_max):
        if random.random() < p:
            return random.randint(-5,5) + vitesse_max
        return vitesse_max
