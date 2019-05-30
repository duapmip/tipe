import numpy as np
import random
from helpers import *

A = 3
B = 1

class Car:

    def __init__(self, temps):
        self._temps = temps
        self._position = []
        self._vitesse = []
        self._acceleration = []

    @property
    def temps(self):
        return self._temps

    @property
    def position(self):
        return self._position

    @property
    def vitesse(self):
        return self._vitesse

    @property
    def acceleration(self):
        return self._acceleration
    
    def set_leader(self, position_init, function):
        self._position = function(self._temps, position_init)[:-1]
        self._vitesse = []
        self._acceleration = []

    
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
                self._position.append(self._position[i-1] + self._vitesse[i] * dt)
                
        self._position = self._position[:-1]
