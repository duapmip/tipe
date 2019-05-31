import abc

class AbstractCar:

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
    
    def set_leader(self, position_init, vitesse_init, function):
        self._position, self._vitesse, self._acceleration = function(self._temps, position_init, vitesse_init)
        
    @abc.abstractmethod
    def set_caracteristiques(self, leader, temps_init, position_init, vitesse_init, vitesse_max):
        pass