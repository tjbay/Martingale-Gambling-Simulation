import matplotlib.pyplot as plt
from matplotlib import rc, rcParams
import random as rn
import numpy as np

#### ---------------------------------------------------

def randomwalk(cost, start, winp, N):
    output = np.zeros(N)
    running_sum = start

    for i in range(N):
        running_sum -= cost
        if rn.random() < winp:
            running_sum += 1
        output[i] = running_sum

    return output

plt.figure(figsize=(12,6))


rn.seed(1)

for num in range(25):
    result = randomwalk(0.5, 0, 18.0/37, 500)
    if result[-1] < 0:
        plt.plot(result, 'r', alpha = .15)
    else:
        plt.plot(result, 'b', alpha = .15)

#plt.title('Random Walk', fontsize=15)
plt.xlabel('Bets', fontsize=15)
plt.ylabel('Money', fontsize=15)
plt.show()


#### ---------------------------------------------------

money = 500
maxbet = 1024000
bet_size = 1
Nbets = 2500
winp = 18.0/37

rn.seed(1)

def gamble(start_money, max_bet, winp, Nbets):
    bet_size = 1
    money = start_money
    output = np.zeros(Nbets)

    for i in range(Nbets):
        if rn.random() < winp:
            money += bet_size
            bet_size = 1
        else:
            money -= bet_size
            bet_size = np.min((2 * bet_size, max_bet))

        output[i] = money

    return output

plt.figure(figsize=(12,6))

for num in range(25):
    result = gamble(500, 256, 18.0/37, 5000)

    if min(result) < 0:
        plt.plot(result, 'r', alpha = .25)
    else:
        plt.plot(result, 'b', alpha = .25)

#plt.title('Gambler Strategy Results', fontsize=15)
plt.xlabel('Bets', fontsize=15)
plt.ylabel('Money', fontsize=15)
plt.show()











