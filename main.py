from Orchestrator import Orchestrator
from leader_functions import * 
from helpers import *

if __name__ == "__main__":
    print("Let's go")
    orchestrator = Orchestrator()
    x_min = 0
    x_max = 1000
    n = 10000
    cars = orchestrator.simulation(x_min, x_max, n, 800, leader_function_1, 500)
    
    temps = creation_temps(x_min, x_max, n)
    creation_positions_graphique([car.position for car in cars], temps)
