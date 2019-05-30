import random

def leader_function_1(temps, position_init):
    positions = []
    a = random.randint(100,400)
    b = random.randint(500,2800)
    c = random.randint(3600,3900)
    for i in range(len(temps)+1):
        if i <= a:
            positions.append(position_init +  9.3 * temps[i])
        else:
            if a<i<=b:
                positions.append(1.5 * temps[i-a] + positions[a])
            else:
                if b<i<=c:
                    positions.append(8 * temps[i-b] + positions[b])
                else:
                    if c<=i<=4500:
                        positions.append(2.2 * temps[i-c] + positions[c])
                    else:
                        positions.append(12 * temps[i-4500] + positions[4500])                   
    return positions
