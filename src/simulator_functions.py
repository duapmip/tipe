from src.helpers import *
import random

# creation de differents types de comportements pour les conditions initiales.

a = 0.000001
def simulator_function_1(i, p, vitesse, position_init_leader, car_factory, cars, temps, model):
    """
    Creation des voitures
    :param p: nombre aleatoire jouant sur l'ecart initiale entre 2 voitures
    :return: objet voiture 
    """
    if i<=23:
        position_init = max(0, min(position_init_leader - p*(i+1) - creation_distance_min(vitesse),position_init_leader - p * (i+2)))
        car = car_factory.create_car(temps, cars[i], a, position_init, model)
    elif 24<=i<=60:
        position_init = max(0, min(position_init_leader - (p+5)*i - creation_distance_min(vitesse),position_init_leader - (p+5) * (i+1)))
        car = car_factory.create_car(temps, cars[i], a, position_init, model)
    else:
        position_init = 0
        car = car_factory.create_car(temps, cars[i], a, position_init, model)
    return car



def simulator_function_2(i, p, vitesse, position_init_leader, car_factory, cars, temps, model):
    """
    Creation des voitures
    :param p: nombre aleatoire jouant sur l'ecart initiale entre 2 voitures
    :return: objet voiture 
    """
    if i<=23:
        position_init = max(0, position_init_leader + p - i*(p + creation_distance_min(vitesse)) - random.random())
        car = car_factory.create_car(temps, cars[i], a, position_init, model)
    else:
        position_init = 0
        car = car_factory.create_car(temps, cars[i], a, position_init, model)
    return car