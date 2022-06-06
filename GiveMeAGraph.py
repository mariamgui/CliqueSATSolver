# Generate a graph has n vertices and there exits a maximal size of c clique in the graph.
# The output is an adjacency matrix saved in xlsx.

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
    workbook = xlsxwriter.Workbook('n'+str(n)+'c'+str(c)+'.xlsx')
    worksheet = workbook.add_worksheet()

    # write a n*n matrix with 0s
    for row in range(n):
        for col in range(n):
            worksheet.write(row, col, 0)

    # write 1s to the corresponding entries for edges
    for e in edges:
        worksheet.write(e[0], e[1], 1)
        worksheet.write(e[1], e[0], 1)
    workbook.close()


GiveMeAGraph(20,5)
