# Generate a graph in xlsx format.
# The graph has n vertices and there exits a maximal size of c clique in the graph.

import xlsxwriter
import random

def GiveMeAGraph(n, c):
    vertices = []
    edges = []

    # create a vertex list
    for v in range(int(n)):
        vertices.append(v)

    # make a loop
    for index, v in enumerate(vertices):
        if index < len(vertices)-1:
            edges.append((v,vertices[index+1]))
        else:
            edges.append((v,vertices[0]))

    # only deal with c greater than 2 
    if c > 2:
        # randomly select c vertices
        clique_vertices = random.sample(vertices, c)
        # adding edges to make these vertices complete in the graph
        # note there may already exist edges from previous vertex to the current vertex
        for index, v1 in enumerate(clique_vertices):
            v2_index = index+1
            # generate edges and check if such edge already exists
            while v2_index < len(clique_vertices):
                v2 = clique_vertices[v2_index]
                if (v1,v2) not in edges and (v2, v1) not in edges:
                    edges.append((v1,v2))
                v2_index+=1

    # export edges to the xlsx
    writeToFile(n, c, edges)

def writeToFile(n, c, edges):
    workbook = xlsxwriter.Workbook(str(n)+'_'+str(c)+'.xlsx')
    worksheet = workbook.add_worksheet()
    
    # write data
    row = 0
    for e in edges:
        worksheet.write(row, 0, e[0])
        worksheet.write(row, 1, e[1]) 
        row += 1
    workbook.close()


GiveMeAGraph(5,3)