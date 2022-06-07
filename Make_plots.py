from GiveMeAGraph import*
from Clique_solver import*

import matplotlib.pyplot as plt

def plot_1():
    # fix n to a small value and then update c from small to bigger value and plot runtime
    n=20
    size_of_clique = 5
    min_c = 5  # inclusive
    max_c = 15  # inclusive

    # make a graph
    GiveMeAGraph(n, size_of_clique)

    File = 'n' + str(n)+ 'c'+ str(size_of_clique) +'.xlsx'

    results = []
    c_list = []
    time_list = []
    # run the solver on each of the c for the same graph, record time each time
    for c in range(min_c, max_c+1):
        query = (File, c)
        c_list.append(c)
        r = Clique_solver(query)
        print(r)
        results.append(r)

    for r in results:
        time_list.append(r[1])

    plt.plot(c_list, time_list)
    # naming the x axis
    plt.xlabel('c')
    # naming the y axis
    plt.ylabel('Running time (s)')
    # giving a title to my graph
    plt.title('Running Time vs c on Graph of size ' + str(n))

    plt.show()

def plot_2():
    # fix c to a small value and update n from small to big value and plot runtime
    c = 5 # used to generate graphes that has clique of size c
    query_c = 15 # used to query clique_solver if clique of size query_c exists
    min_n = 20  # inclusive
    max_n = 25  # inclusive

    if c >= min_n:
        print('c has to be smaller than or equal to min_n')

    results = []
    n_list = []
    time_list = []
    for n in range(min_n, max_n+1):
        # make a graph
        GiveMeAGraph(n, c)

        File = 'n' + str(n)+ 'c'+ str(c) +'.xlsx'

        # run the solver on the same c for different graphes of size n, record time each time
        query = (File, query_c)
        r = Clique_solver(query)
        print(r)
        n_list.append(n)
        results.append(r)

    for r in results:
        time_list.append(r[1])

    plt.plot(n_list, time_list)
    # naming the x axis
    plt.xlabel('n')
    # naming the y axis
    plt.ylabel('Running time (s)')
    # giving a title to my graph
    plt.title('Running Time vs n on queries made by same c=' + str(query_c))

    plt.show()

#plot_1()
plot_2()