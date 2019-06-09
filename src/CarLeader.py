"""CarLeader.py"""

import abc
from src.AbstractCar import AbstractCar

# Creation d'une classe poour attribuer la position, la vitesse et l'acceleration de la 1ere voiture (leader)

class CarLeader(AbstractCar):
    """Classe correspondante a la voiture leader.
    Permet d'assigner l'acceleration, la vitesse et la position.

    Attributs:
        temps (list): Liste du temps.
    """

    def __init__(self, temps):
        super().__init__(temps)
        
    
    def set_leader(self, position_init, vitesse_init, function):
        """Creation positions, vitesses et acceleration

        Args:
            position_init (int): Position initiale
            vitesse_init (int): Vitesse initiale
            function (function): fonction du leader                     
        
        Returns:
            list: positions
            list: vitesses
            list: accelerations
        """
        self._position, self._vitesse, self._acceleration = function(self._temps, position_init, vitesse_init)