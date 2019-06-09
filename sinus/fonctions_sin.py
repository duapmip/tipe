"""fonctions_sin.py"""

import numpy as np
import random
import matplotlib.pyplot as plt
from random import randint

def creation_temps(x_min, x_max, n):
    """Creation du temps
    
    Args:
        x_min (int): debut de la simulation
        x_max (int): Fin de la simulation
        n (int): Pas de la simulation

    Returns:
        list: Temps
    """
    temps = []
    for i in range(0, n+1):
        temps.append(x_min + ((i * (x_max - x_min)) / n))
    return temps


def creation_distance_min(p, distance_min):
    """Creation de la distance moyenne
    
    Args:
        p (float): Nombre aleatoire
        distance_min (int): Distance minimale

    Returns:
        int: Distance minimale
    """
    if random.random() < p:
        return randint(1,5) + distance_min
    return distance_min

def creation_vitesse_max(p, vitesse_max):
    """Creation vitesse maximum

        Args:
            p (float): Nombre aleatoire
            vitesse_max (int): Vitesse maximum autorisee
        
        Returns:
            int: Vitesse maximum
        """
    if random.random() < p:
        return randint(-5,5) + vitesse_max
    return vitesse_max

def creation_positions_voiture_1(temps, n, position_initiale):
    """Creation de la position de la premiere voiture
    
    Args:
        temps (list): Liste de temps
        n (int): Pas de la simulation
        position_init (int): Position initiale

    Returns:
        list: Positions de la 1ere voiture
    """
    positions = []
    for i in range(n+1):
        positions.append(position_initiale +  4 * temps[i] + (np.cos(temps[i])) + (np.sin(temps[i])))
    return positions


def creation_positions_voiture_2(positions_voiture_1, n, temps_initiale, distance_min, vitesse_max, temps):
    """Creation de la position d une voiture
    
    Args:
        positions_voiture_1 (list): Positions de la voiture de devant
        n (int): Pas de la simulation
        temps_init (int): Temps initiale
        distance_min (int): Distance minimale
        vitesse_max (int): Vitesse maximale
        temps (list): Liste de temps

    Returns:
        list: Positions d une voiture
    """
    position = [0]
    vitesse = 0
    distance_min = creation_distance_min(0.8, distance_min)
    vitesse_max = creation_vitesse_max(0.9, vitesse_max)
    for i in range(0, n+1):
        if temps[i] <= temps_initiale:
            position.append(0)
        else:
            distance = positions_voiture_1[i]-position[i-1]
            if distance < distance_min:
                vitesse = 0
            else:
                vitesse = vitesse_max * (1 - np.exp((-distance + distance_min) / (5 * distance_min)))
            position.append(min(positions_voiture_1[i] - distance_min , vitesse * temps[i] + position[i-1]))
    return position[0: -1]


def creation_positions(position_voiture_1, nombre_voitures, distance_min , vitesse_max, temps):
    """Creation des position des voitures
    
    Args:
        positions_voiture_1 (list): Positions de la 1ere voiture
        nombre_voitures (int): Nombre de voitures
        distance_min (int): Distance minimale
        vitesse_max (int): Vitesse maximale
        temps (list): Liste de temps

    Returns:
        list: Positions des voitures
    """
    positions = [position_voiture_1]
    for i in range(0, nombre_voitures):
        positions.append(creation_positions_voiture_2(positions[i], 500, i + random.random(), distance_min, vitesse_max, temps))
    return positions

def creation_positions_graphique(positions, temps):
    """Creation des graphiques des positions
    
    Args:
        positions (list): Liste de liste des positions des voitures
        temps (list): Liste de temps
    """
    for position in positions:
        plt.title('Positions des voitures')
        plt.xlabel('position (m)')
        plt.ylabel('temps (s)')
        plt.plot(position, temps, linestyle='solid')
