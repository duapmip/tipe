import random

# def leader_function_1(temps, position_init):
#     positions = []
#     a = random.randint(100,400)
#     b = random.randint(500,2800)
#     c = random.randint(3600,3900)
#     for i in range(len(temps)+1):
#         if i <= a:
#             positions.append(position_init +  9.3 * temps[i])
#         else:
#             if a<i<=b:
#                 positions.append(1.5 * temps[i-a] + positions[a])
#             else:
#                 if b<i<=c:
#                     positions.append(8 * temps[i-b] + positions[b])
#                 else:
#                     if c<=i<=4500:
#                         positions.append(2.2 * temps[i-c] + positions[c])
#                     else:
#                         positions.append(9 * temps[i-4500] + positions[4500])                   
#     return positions


def leader_function_1(temps, position_init, vitesse_init):
    positions = [position_init]
    vitesses = [vitesse_init]
    accelerations = []
    a = random.randint(300,400)
    b = random.randint(500,1800)
    c = random.randint(3600,3900)
    dt = temps[1] - temps[0]
    for i in range(len(temps)):
        if i <= a:
            accelerations.append(-0.4)
        else:
            if a<i<=b:
                accelerations.append(0.08)
            else:
                if b<i<=c:
                    accelerations.append(-0.04)
                else:
                    if c<=i<=4500:
                        accelerations.append(-0.03)
                    else:
                        accelerations.append(0.06)
        vitesses.append(accelerations[i] * dt + vitesses[i])
        positions.append(vitesses[i] * dt + positions[i])                   
    return positions[:-1], vitesses, accelerations