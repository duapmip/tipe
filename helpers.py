import matplotlib.pyplot as plt

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


def creation_positions_graphique(positions, temps):
    """
    Creation des graphiques des positions
    :param positions: liste de liste des positions des voitures
    :param temps: liste de temps
    :return: graphique des positions
    """
    for position in range(0, len(positions), 1):
        plt.plot(positions[position][::30], temps[::30], 'o', color='black', markersize=0.5)
        plt.plot(positions[position], temps)
    plt.show()