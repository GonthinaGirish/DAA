lst = {}
def makeSet(i): 
    lst[i] = i
def Find(k): 
    if lst[k] == k:
        return k
    return Find(lst[k])
def Union(a, b):
    x = Find(a)
    y = Find(b)
    lst[x] = y
def kruskalAlgo(edges, N):
    total_min_weight=0
    MST = []
    for i in range(N):
        makeSet(i)
    index = 0
    edges.sort(key=lambda x: x[2])
    while len(MST) != N - 1:
        (u, v, weight) = edges[index]
        index = index + 1
        x = Find(u)
        y = Find(v)
        
        if x != y:
            MST.append((u, v, weight))
            Union(x, y)
            total_min_weight+=weight
        for u,v, weight in MST:
            #total_min_weight+=weight
            print("%d - %d = %d" % (u, v, weight))
    return MST,total_min_weight
    
edges = [
    (0, 1, 1), (0, 2, 2), (0, 3, 1),
    (0, 4, 1), (0, 5, 2), (0, 6, 1),
    (1, 2, 2), (1, 6, 2), (2, 3, 1),
    (3, 4, 2), (4, 5, 2), (5, 6, 1)]
N = 7
mst,min_w = kruskalAlgo(edges, N)
print('Edges in the constructed MST:',mst)
print('Minimum Cost Spanning Tree:',min_w)
