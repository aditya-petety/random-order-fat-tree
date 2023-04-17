# random-order-fat-tree

Run this with python nx_fat_tree.py depth degree iterations.

For example to if I want my tree to have depth 4, degree of each node 10 and I want to run this for 10 iterations, I run "python nx_fat_tree.py 4 10 10".

The output gives total number of nodes in graph, the max load in each iteration and the average max load over all iterations. 


For symmetric instance with greedy algorithm over the load of vertices, run "python lb_symmetric_instance.py" in the terminal. By default it runs for 1000 iterations and 2^20 nodes. To change the number of nodes to 2^k replace depth in line 8 by value of k. To run a different number of iterations, edit line 9.
