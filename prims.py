V = 6
G = [[0, 9, 75, 0, 0,25],
     [9, 0, 95, 19, 42,95],
     [75, 95, 0, 51, 66,81],
     [0, 19, 51, 0, 31,65],
     [0, 42, 66, 31, 0,8]]
     [26,35,]
selected = [0, 0, 0, 0, 0,0]
no_edge = 0
selected[0] = True
print("Edge : Weight\n")
while (no_edge < V - 1):
    minimum = 1000
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):  
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    selected[y] = True
    no_edge += 1
