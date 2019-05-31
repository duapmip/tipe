from src.AbstractCar import AbstractCar


class CarIDM(AbstractCar):

    def __init__(self):
        super().__init__()

    def set_caracteristiques(self, leader, temps_init, position_init, vitesse_init, vitesse_max):
        self._position.append(position_init)
        self._vitesse.append(vitesse_init)
        acceleration_max = 1.5
        for i in range(0, len(self._temps)):
            dt = self._temps[i] - self._temps[i-1]
            dv = self._vitesse[i] - leader.vitesse[i]
            distance_min = creation_distance_min(0)
            if self._temps[i] < temps_init:
                self._position.append(position_init)
                self._vitesse.append(0)
                self._acceleration.append(0)
            else:
                distance = leader.position[i-1] - self._position[i-1]
                s_etoile = distance_min + (self._vitesse[i] * dv) / 2 * np.sqrt(acceleration_max)
                acceleration_libre = acceleration_max * (1 - (self._vitesse[i] / vitesse_max)**4)
                acceleration_condi = - acceleration_max * (s_etoile / distance)**2
                self._acceleration.append(acceleration_libre + acceleration_condi)
                self._vitesse.append(max(self._acceleration[i] * dt + self._vitesse[i], 0))
                self._position.append(self._position[i] + self._vitesse[i] * dt)

        self._position = self._position[:-1]