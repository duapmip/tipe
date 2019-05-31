import abc
from src.AbstractCar import AbstractCar

class CarLeader(AbstractCar):

    def __init__(self, temps):
        super().__init__(temps)
        
    
    def set_leader(self, position_init, vitesse_init, function):
        self._position, self._vitesse, self._acceleration = function(self._temps, position_init, vitesse_init)