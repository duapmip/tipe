"""main.py"""

import numpy as np
import matplotlib.pyplot as plt
from fonctions_sin import *

temps = creation_temps(0, 50, 500)

position_voiture_1 = creation_positions_voiture_1(temps, 500, 10) 

positions = creation_positions(position_voiture_1, 50, 2, 25, temps)

plt.xlim(0,250)
plt.ylim(0,50)
creation_positions_graphique(positions, temps)
plt.show()
