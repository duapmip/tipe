import matplotlib.pyplot as plt
from datetime import datetime

def creation_distance_min(vitesse):
    """
    Creation d'une distance minimale
    :param vitesse: vitesse de la voiture
    :return: la distance minimale avec la voiture precedante
    """
    distance_min = (((vitesse*0.36)**2)/2) + 1
    return distance_min

def creation_temps(x_min, x_max, n):
    """
    Creation d'une liste de temps entre x_min et x_max avec n valeurs
    """
    temps = []
    for i in range(0, n+1):
        temps.append(x_min + ((i * (x_max - x_min)) / n))
    return temps


def creation_positions_graphique(positions, temps):
    """
    Creation des graphiques des positions
    :param positions: liste de liste des positions des voitures
    :param temps: liste de temps
    :return: graphique des positions (temps en ordonnee pour ameliorer la visibilite)
    """
    for position in range(0, len(positions), 1):
        plt.plot(positions[position], temps)
    plt.xlim(0,12000)
    plt.ylim(0,1000)
    plt.title('Positions des voitures')
    plt.xlabel('position (m)')
    plt.ylabel('temps (s)')
    plt.show()


def creation_vitesse_moyenne_graphique(cars, temps):
    """
    Creation de la vitesse moyenne
    :param positions: liste de liste des positions des voitures
    :param temps: liste de temps
    :return: graphique de la vitesse moyenne en focntion du temps
    """
    s = 0
    v = []
    n = len(temps)
    for i in range(0, n):
        s = 0
        for car in cars:
            s = s + car.vitesse[i]
        v.append(s/len(cars))
    plt.plot(temps, v)
    plt.xlim(0,1000)
    plt.ylim(0,30)
    plt.title('vitesse moyenne des voitures')
    plt.xlabel('temps (s)')
    plt.ylabel('vitesse moyenne (m/s)')
    plt.show()


def creation_distance_moyenne_graphique(cars, temps):
    """
    Creation de la distance moyenne
    :param positions: liste de liste des positions des voitures
    :param temps: liste de temps
    :return: graphique de la distance moyenne en fonction du temps
    """
    s = 0
    d = []
    n = len(temps)
    for i in range(0, n):
        s = 0
        for j in range(len(cars)-1):
            s = s + cars[j].position[i] - cars[j+1].position[i]
        d.append(s/(len(cars)-1))
    plt.plot(temps, d)
    plt.xlim(0,1000)
    plt.ylim(0,30)
    plt.title('distance moyenne des voitures')
    plt.xlabel('temps (s)')
    plt.ylabel('distance moyenne (m)')
    plt.show()