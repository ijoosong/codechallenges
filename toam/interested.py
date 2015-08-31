from igraph import *
def setup(x, y):
#    x = 300
#    y = 250
    li = []

    for i in range(x-1):
        for j in range(y):
            li.append((i+j*x, i+1+j*x))
    for i in range(x):
        for j in range(y-1):
            li.append((i+j*x, i+x+j*x))

    g = Graph()
    g.add_vertices(x*y)
    g.add_edges(li)

    return g
