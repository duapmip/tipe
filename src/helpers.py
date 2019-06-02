import matplotlib.pyplot as plt
from datetime import datetime

def creation_distance_min(vitesse):
    """
    Creation d'une distance minimale
    :param p: probabilite que la distance minimale change (plus p est grand, plus la distance minimale a de chance de changer) 
    :param distance_min: distance minimale autorisee
    :return: la distance minimale entre 2 voitures  
    """
    distance_min = (((vitesse*0.36)**2)/2) + 1
    return distance_min

def creation_temps(x_min, x_max, n):
    temps = []
    for i in range(0, n+1):
        temps.append(x_min + ((i * (x_max - x_min)) / n))
    return temps


def creation_positions_graphique(positions, temps, save=False):
    """
    Creation des graphiques des positions
    :param positions: liste de liste des positions des voitures
    :param temps: liste de temps
    :return: graphique des positions
    """
    for position in range(0, len(positions), 1):
        # plt.plot(positions[position][::30], temps[::30], 'o', color='black', markersize=0.5)
        plt.plot(positions[position], temps)
    plt.xlim(0,12000)
    plt.ylim(0,1000)
    plt.title('Positions des voitures')
    plt.xlabel('position (m)')
    plt.ylabel('temps (s)')
    plt.show()


def creation_vitesse_moyenne_graphique(cars, temps, save=False):
    s = 0
    a = []
    n = len(temps)
    for i in range(0, n):
        s = 0
        for car in cars:
            s = s + car.vitesse[i]
        a.append(s/len(cars))
    plt.plot(temps, a)
    plt.xlim(0,1000)
    plt.ylim(0,30)
    plt.title('vitesses des voitures')
    plt.xlabel('temps (s)')
    plt.ylabel('vitesse (m)')
    if save:
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        filename = f"img/vitesse_moyenne_{timestamp}.png"
        plt.set_size_inches(18.5, 10.5)
        plt.savefig(filename)
    plt.show()