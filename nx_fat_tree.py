import networkx as nx
import sys
import random

max_array = []

n = int(sys.argv[3])
d = int(sys.argv[1])
degree = int(sys.argv[2])

node = [pow(degree,i) for i in range(d)]
nodes = sum(node)
print(nodes)

#print(sys.argv)

for i in range(n):

    G = nx.Graph()

    #d = 6
    #degree = int(3*d*d)
    #degree = 12
    #print(degree)
    node = [pow(degree,i) for i in range(d)]
    nodes = sum(node)
    #print(nodes)

    depth = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]

    r = 0

    for i in range(d-1):
        for k in range(0,pow(degree,i)):
            for j in range(0,degree):
                G.add_edge("%s%s" % (depth[i],k), "%s%s" % (depth[i+1],k*degree+j))

    online_edge = random.sample(list(G.edges()), len(G.edges()))

    maxi = 0

    #print(online_edge[0])
    #print(list(G.edges())[0])

    H = nx.Graph()
    for i in list(G.nodes()):
        H.add_node(i)
    #print(len(H.nodes()))

    load = {}

    for i in list(G.nodes()):
        load[i] = 0

    #print(load["c25"])
    k=0
    for edge in online_edge:
        #print(edge)
        k +=1
        if k%100 == 0:
            print(k)
        sum1 = len(nx.node_connected_component(H,edge[0]))
        sum2 = len(nx.node_connected_component(H,edge[1]))
        #print(sum1)
        #print(sum2)
        if sum1 == sum2:
            x = random.randint(0,1)
            load[edge[x]] += 1
            #print(x)
        if sum1 > sum2:
            load[edge[1]] += 1
        if sum2 > sum1:
            load[edge[0]] += 1
        #dict[edge[1]].load += 1
        #print(dict[edge[0]].load)
        if maxi < max(load[edge[0]], load[edge[1]]):
            maxi = max(load[edge[0]], load[edge[1]])
        H.add_edge(edge[0],edge[1])
        #print(load)

    max_array.append((max(load.values())))
    #print(load)
print(max_array)
print(sum(max_array)/len(max_array))
