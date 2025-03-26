import numpy as np
import matplotlib.pyplot as plt
N = 10000 #total number of people in population
S = [9999] #susceptible people
I = [1]  #infected people
R = [0]  #people who were infected and have already recovered
b = 0.3 #infection probability upon coontact
r = 0.05 #recovery probability of an infected person, and is assumed to be immune to the disease
#calculate the infection rate first
for t in range(1000):
    i=I[-1]/N #infected proportion
    new_infected = np.random.binomial(S[-1],b*i)
    new_recover = np.random.binomial(I[-1],r)
    S.append(S[-1] - new_infected)
    I.append(I[-1] + new_infected - new_recover)
    R.append(R[-1] + new_recover)

#draw the graph
plt.figure(figsize=(10, 6), dpi=150)
plt.plot(S, label='Susceptible')
plt.plot(I, label='Infected')
plt.plot(R, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of People in the Population')
plt.title('SIR Model Simulation')
plt.legend()
plt.grid()
plt.savefig("SIR_model.png", format="png")
plt.show()