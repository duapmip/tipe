import random

def leader_function_1(temps, position_init, vitesse_init):
    positions = [position_init]
    vitesses = [vitesse_init]
    accelerations = []
    a = 280
    b = 850
    c = 3700
    dt = temps[1] - temps[0]
    for i in range(len(temps)):
        if vitesses[i] > 0:
            if i <= a:
                accelerations.append(-0.6)
            if a<i<=b:
                accelerations.append(0.24)
            if b<i<=c:
                accelerations.append(-0.04)
            if c<=i<=4500:
                accelerations.append(-0.03)
            else:
                accelerations.append(0)
        else:
            accelerations.append(0.1)
        vitesses.append(accelerations[i] * dt + vitesses[i])
        positions.append(vitesses[i] * dt + positions[i])                   
    return positions[:-1], vitesses, accelerations


def leader_function_2(temps, position_init, vitesse_init):
    positions = [position_init]
    vitesses = [vitesse_init]
    accelerations = []
    a = 280
    b = 460
    c = 600
    d = 2500 
    e = 2850
    dt = temps[1] - temps[0]
    for i in range(len(temps)):
        if vitesses[i] > 0:
            if i <= a:
                accelerations.append(0.06)
            if a<i<=b:
                accelerations.append(-1.1)
            if b<i<=c:
                accelerations.append(0.02)
            if c<=i<=d:
                accelerations.append(0.08)
            if d<=i<=e:
                accelerations.append(-0.43)
            if e<=i<=3000:
                accelerations.append(-0.03)
            else:
                accelerations.append(0.001)
        else:
            accelerations.append(0.1)
        vitesses.append(accelerations[i] * dt + vitesses[i])
        positions.append(vitesses[i] * dt + positions[i])                   
    return positions[:-1], vitesses, accelerations