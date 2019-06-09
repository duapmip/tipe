"""CarFactory.py"""

from src.CarPerso import CarPerso
from src.CarIDM import CarIDM
from src.CarLeader import CarLeader
import random


class CarFactory:
    """Classe permettant de definir toutes les voitures 
    """

    def __init__(self):
        pass

    
    def create_leader(self, temps, position_init, vitesse_init, function):
        """Creation du leader

        Args:
            temps (list): Liste de temps
            position_init (int): Position initiale
            vitesse_init (int) : Vitesse initiale
            function (function): Fonction du leader
        
        Returns:
            CarLeader: Voiture leader
        """
        leader = CarLeader(temps)
        leader.set_leader(position_init, vitesse_init, function)
        return leader


    def create_car(self, temps, leader, temps_init, position_init, model):
        """Creation d'une voiture

        Args:
            temps (list): Liste de temps
            leader (CarLeader): Voiture leader
            temps_init (int) : Temps initiale
            position_init (int): Position initiale
            model (str): Modele
             
        
        Returns:
            CarPerso: Voiture 
        """
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
        """Creation vitesse maximum

        Args:
            p (float): Nombre aleatoire
            vitesse_max (int): Vitesse maximum autorisee
        
        Returns:
            int: Vitesse maximum
        """
        if random.random() < p:
            return random.randint(-5,5) + vitesse_max
        return vitesse_max
