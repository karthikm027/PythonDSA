# Matrix structure 
# To find shortest path between all the vertices

def printSolution(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if (distance[i][j] == 999):
                print("INF", end=" ")
            else:
                print(distance[i][j], end = " ")
        print(" ")

def floydWarshall(nV, G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    printSolution(nV, distance)

nV = 4
G = [[0, 8, 999, 1],
     [999, 0, 1, 999],
     [4, 999, 0, 999],
     [999, 2, 9, 0]]

floydWarshall(nV, G)