from Orchestrator import Orchestrator
from leader_functions import * 
from helpers import *

if __name__ == "__main__":
    print("Let's go")
    x_min = 0
    x_max = 1000
    n = 10000
    position_init = 800
    leader_function = leader_function_1
    nb_voitures = 500

    orchestrator = Orchestrator(x_min, x_max, n)
    cars = orchestrator.simulation(position_init, leader_function_1, nb_voitures)
    creation_positions_graphique([car.position for car in cars], orchestrator.temps)
