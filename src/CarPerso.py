import numpy as np
import random
from src.helpers import *

from src.AbstractCar import AbstractCar
A = 5
B = 2


class CarPerso(AbstractCar):
    """
    Classe correspondante au modele de l'Intelligent Driver Model (IDM).
    Permet d'assigner l'acceleration, la vitesse et la position d'apres le modele Personnel a chaque instant.
    """

    def __init__(self, temps):
        super().__init__(temps)

    def set_caracteristiques(self, leader, temps_init, position_init, vitesse_init, vitesse_max):
        self._position.append(position_init)
        self._vitesse.append(vitesse_init)
        for i in range(0, len(self._temps)):
            distance_min = creation_distance_min(self._vitesse[i])
            dt = self._temps[i] - self._temps[i-1]
            if self._temps[i] < temps_init:
                self._position.append(position_init)
                self._vitesse.append(0)
                self._acceleration.append(0)
            else:
                distance = leader.position[i-1] - self._position[i-1]
                self._acceleration.append(A * (1 - B * np.exp(-distance + distance_min))*(1 - np.exp((self._vitesse[i] - vitesse_max) / vitesse_max)))
                self._vitesse.append(max(self._acceleration[i] * dt + self._vitesse[i], 0))
                self._position.append(self._position[i] + self._vitesse[i+1] * dt)
                
        self._position = self._position[:-1]
