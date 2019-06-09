import abc

class AbstractCar:
    """
    Classe commune aux classes CarLeader, CarIDM, CarPerso (une voiture possede toujours une position, une vitesse et une acceleration)
    """

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
    
    @abc.abstractmethod
    def set_leader(self, position_init, vitesse_init, function):
        pass
        
    @abc.abstractmethod
    def set_caracteristiques(self, leader, temps_init, position_init, vitesse_init, vitesse_max):
        pass