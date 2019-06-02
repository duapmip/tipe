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
    print("Let's go")
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--x_min", default=0, type=int)
    argument_parser.add_argument("--x_max", default=1000, type=int)
    argument_parser.add_argument("--n", default=10000, type=int)
    argument_parser.add_argument("--position_init", default=800, type=int)
    argument_parser.add_argument("--nombre_voitures", default=100, type=int)
    argument_parser.add_argument("--vitesse", default=20, type=int)
    argument_parser.add_argument("--model", default="perso", type=str)
    argument_parser.add_argument("--leader_function", choices=LEADER_FUNCTION.keys(), default="leader_function_2")
    argument_parser.add_argument("--simulator_function", choices=SIMULATOR_FUNCTION.keys(), default="simulator_function_2")
    args = argument_parser.parse_args()
    
    x_min = args.x_min
    x_max = args.x_max
    n = args.n
    position_init = args.position_init
    nombre_voitures = args.nombre_voitures
    vitesse = args.vitesse
    model = args.model

    leader_function = LEADER_FUNCTION[args.leader_function]
    simulator_function = SIMULATOR_FUNCTION[args.simulator_function]

    simulator = Simulator(x_min, x_max, n)
    cars = simulator.simulation(nombre_voitures, position_init, vitesse, leader_function, simulator_function, model)

    creation_positions_graphique([car.position for car in cars], simulator.temps)
    creation_vitesse_moyenne_graphique(cars, simulator.temps)