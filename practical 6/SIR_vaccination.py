import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N = 10000          # population
I0 = 1             # initial infected people
S0 = N - I0        # initial susceptible
R0 = 0             # initial recovered people
beta = 0.3         # infection rate
gamma = 0.05       # recovery rate
time_steps = 1000  # time

# different results on different vaccination rates
vaccination_rates = [0,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1.00]
plt.figure(figsize=(10, 6))
colors = cm.viridis(np.linspace(0, 1, len(vaccination_rates)))  # using viridis colormap

#different initial values in different vaccination rate
for idx, vaccination_rate in enumerate(vaccination_rates): #correlates each vaccination rate with a different color
    vaccinated = int(vaccination_rate * N)
    S0 = N - I0 - vaccinated
    S = [S0]
    I = [I0]
    R = [R0]
    #time step simulation
    for t in range(1, time_steps):
        if S[-1] <= 0: #when vaccination rate is 100, initial value of S will be less than 0
            S.append(0)
            continue
        new_infected = np.random.binomial(S[-1], beta * I[-1] / N) #calculate infected people
        new_recovered = np.random.binomial(I[-1], gamma)
        S.append(S[-1] - new_infected)
        I.append(I[-1] + new_infected - new_recovered)
        R.append(R[-1] + new_recovered)
    
    # draw curves of different vaccination rate
    plt.plot(I,label=f"vaccination rate {vaccination_rate*100}%",color=colors[idx])

plt.xlabel("time")
plt.ylabel("infected people")
plt.title("SIR modle with vaccination")
plt.legend()
plt.show()
