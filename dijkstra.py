class dj():
    def __init__(self,vertices):
        self.v = vertices
        self.g = [[0 for column in range(vertices)]
                    for row in range(vertices)]
    def printsol(self,dist):
        print("vertex \t Distance from source")
        for n in range(self.v):
          print(n+1, "\t\t",dist[n])   
    def mindistance(self, dist, visited):
        min = 1e5
        for i in range(self.v):
            if dist[i] < min and visited[i] == False:
                min = dist[i]
                minindex = i
        return minindex
    def djalgo(self, src):
        dist = [1e5]*self.v
        dist[src] = 0
        visited = [False]*self.v
        for count in range(self.v):
            u = self.mindistance(dist,visited)
            visited[u] = True
            for j in range(self.v):
                if(self.g[u][j] > 0 and visited[j] == False and dist[j] > dist[u] + self.g[u][j]):
                    dist[j] = dist[u] + self.g[u][j]
        self.printsol(dist)    
d = dj(6)
d.g =[[0,3,2,5,0,0],
    [3,0,0,1,4,0],
    [2,0,0,2,0,1],
    [5,1,2,0,3,0],
    [0,4,0,3,0,2],
    [0,0,1,0,2,0]]
d.djalgo(0)
