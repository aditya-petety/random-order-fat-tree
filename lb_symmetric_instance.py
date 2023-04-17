import networkx as nx
import sys
import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

depth = 20
n=1000

tot_nodes = pow(2,depth)

G = nx.Graph()

for j in range(1,depth+1):
    for i in range(tot_nodes):
        if (pow(2,j)*i + pow(2,j-1) < tot_nodes):
            G.add_edge(pow(2,j)*i, pow(2,j)*i+pow(2,j-1))


load = {}

makespan = []
attempt = []


for z in range(n):
    print(z)
    attempt.append(z)
    for i in G.nodes():
        load[i] = 0
    online_edge = random.sample(list(G.edges()), len(G.edges()))
    for e in online_edge:
        if load[e[0]] > load[e[1]]:
            load[e[1]] += 1
        elif load[e[0]] < load[e[1]]:
            load[e[0]] += 1
        elif load[e[0]] == load[e[1]]:
            load[e[random.randint(0,1)]] += 1
    maxi = 0
    for i in G.nodes():
        if load[i] > maxi:
            maxi = load[i]
    makespan.append(maxi)

#plt.plot(attempt, makespan)
print(Counter(makespan))

