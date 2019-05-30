from Simulator import Simulator
from leader_functions import * 
from helpers import *
from simulator_functions import *

if __name__ == "__main__":
    print("Let's go")
    x_min = 0
    x_max = 1000
    n = 10000
    position_init = 800
    leader_function = leader_function_1
    simulator_function = simulator_function_2
    nombre_voitures = 500
    vitesse = 20

    simulator = Simulator(x_min, x_max, n)
    cars = simulator.simulation(nombre_voitures, position_init, vitesse, leader_function, simulator_function)
    creation_positions_graphique([car.position for car in cars], simulator.temps)
