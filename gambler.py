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

# rn.seed(1)

win_counter = 0.0
num_simulations = 200
cum_sum_of_sims = 0

for num in range(num_simulations):
    result = randomwalk(0.5, 0, 18.0/37, 500)
    cum_sum_of_sims += result[-1]
    if result[-1] < 0:
        plt.plot(result, 'r', alpha = .15)
    else:
        win_counter += 1
        plt.plot(result, 'b', alpha = .15)

win_percent = 100*win_counter/num_simulations
avg_loss = -1.0*cum_sum_of_sims/num_simulations

print("Only {}% of bettors have postive resutls after {} bets".format(win_percent, num_simulations))
print("The average result of 500 bets is a loss of {} dollars".format(avg_loss))

plt.title('Outcomes of 500 equals bets on Roulette', fontsize=15)
plt.xlabel('Bets', fontsize=15)
plt.ylabel('Money', fontsize=15)
plt.savefig('roulette_random_walk.pdf', bbox_inches='tight')
plt.show()


#### ---------------------------------------------------

money = 500
maxbet = 1024
bet_size = 1
Nbets = 2500
winp = 18.0/37

# rn.seed(1)

def gamble(start_money, max_bet, winp, Nbets):
    bet_size = 1
    money = start_money
    output = np.zeros(Nbets)

    for i in range(Nbets):

        if money < 0:
            pass
        elif rn.random() < winp:
            money += bet_size
            bet_size = 1
        else:
            money -= bet_size
            bet_size = np.min((2 * bet_size, max_bet))
            if bet_size > money:
                bet_size = money

        output[i] = money

    return output

plt.figure(figsize=(12,6))

N_losers = 0
N_sims = 200

for num in range(N_sims):
    result = gamble(500, 256, 18.0/37, 5000)

    if min(result) < 0:
        N_losers += 1
        plt.plot(result, 'r', alpha = .25)
    else:
        plt.plot(result, 'b', alpha = .25)

plt.title('Martingdale Outcome', fontsize=15)
plt.xlabel('Number of Bets', fontsize=15)
plt.ylabel('Money', fontsize=15)
plt.savefig('outcome.pdf', bbox_inches='tight')
plt.show()


print("After 5000 bets, {}% of bettors lost all their money".format(100.0*N_losers/N_sims))










