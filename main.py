import argparse
from src.Simulator import Simulator
from src.leader_functions import * 
from src.helpers import *
from src.simulator_functions import *


LEADER_FUNCTION = {
    "leader_function_1" : leader_function_1,
    "leader_function_2" : leader_function_2 
}

SIMULATOR_FUNCTION = {
    "simulator_function_1" : simulator_function_1,
    "simulator_function_2" : simulator_function_2 
}

if __name__ == "__main__":
    x_min = 0
    x_max = 1000
    n = 10000
    position_init = 800
    nombre_voitures = 500
    vitesse = 20
    model = "perso"
    leader_function = leader_function_2
    simulator_function = simulator_function_1

    simulator = Simulator(x_min, x_max, n)
    cars = simulator.simulation(nombre_voitures, position_init, vitesse, leader_function, simulator_function, model)
    
    creation_positions_graphique([car.position for car in cars], simulator.temps)
    creation_vitesse_moyenne_graphique(cars, simulator.temps)
    creation_distance_moyenne_graphique(cars, simulator.temps)
