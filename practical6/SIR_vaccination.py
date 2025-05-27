import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N = 10000          # total population
I0 = 1             # initial number of infected individuals
R0 = 0             # initial number of recovered individuals
beta = 0.3         # infection probability upon contact
gamma = 0.05       # recovery probability per time step
time_steps = 1000  # number of time steps to simulate

# Vaccination simulation 
vaccination_rates = [0, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00]
plt.figure(figsize=(10, 6))
colors = cm.viridis(np.linspace(0, 1, len(vaccination_rates)))

# Simulate the model for each vaccination rate
for idx, vaccination_rate in enumerate(vaccination_rates):
    vaccinated = int(vaccination_rate * N)
    S0 = N - I0 - vaccinated
    S = [S0]
    I = [I0]
    R = [R0]

    for t in range(1, time_steps):
        if S[-1] <= 0:
            S.append(0)
            I.append(0)
            R.append(R[-1])
            continue

        new_infected = np.random.binomial(S[-1], beta * I[-1] / N)
        new_recovered = np.random.binomial(I[-1], gamma)
        S.append(S[-1] - new_infected)
        I.append(I[-1] + new_infected - new_recovered)
        R.append(R[-1] + new_recovered)

    # Plot the number of infected individuals over time
    plt.plot(I, label=f"vaccination rate {vaccination_rate*100:.0f}%", color=colors[idx])

# Plotting 
plt.xlabel("Time")
plt.ylabel("Number of Infected Individuals")
plt.title("SIR Model with Varying Vaccination Rates")
plt.legend()
plt.tight_layout()
plt.show()