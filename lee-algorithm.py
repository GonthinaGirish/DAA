from collections import deque
ROW = 5
COL = 5

# To store cell cordinates
class Cell:
	def __init__(self,x: int, y: int):
		self.x = x
		self.y = y

# Declaring Queue to be used in BFS
class queueNode:
	def __init__(self,pt: Cell, dist: int):
		self.pt = pt # Cell coordinates
		self.dist = dist # Cell's distance from the source

# Check whether given cell(row,col) is a valid cell or not
def checkValid(row: int, col: int):
	return ((row >= 0) and (row < ROW) and (col >= 0) and (col < COL))

# These arrays show the 4 possible movement from a cell
rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]

# Function to find the shortest path between source cell and destination cell. 
def bfsLee(mat, src: Cell, dest: Cell):
	
	# Checking if source and destination cell have value 1 
	if mat[src.x][src.y]!=1 or mat[dest.x][dest.y]!=1:
		return -1
	
	visited = [[False for i in range(COL)] 
					for j in range(ROW)]
	
	# Mark the source cell as visited 
	visited[src.x][src.y] = True
	
	# Create a queue for BFS 
	q = deque()
	
	# Distance of source cell is 0
	s = queueNode(src,0)
	q.append(s) # Enqueue source cell
	
	# Perform BFS starting from source cell 
	while q:

		curr = q.popleft() # Dequeue the front cell
		
		# If we have reached the destination cell, return the final distance 
		pt = curr.pt
		if pt.x == dest.x and pt.y == dest.y:
			return curr.dist
		
		# Otherwise enqueue its adjacent cells with value 1 
		for i in range(4):
			row = pt.x + rowNum[i]
			col = pt.y + colNum[i]
			
			# Enqueue valid adjacent cell that is not visited
			if (checkValid(row,col) and
			mat[row][col] == 1 and
				not visited[row][col]):
				visited[row][col] = True
				Adjcell = queueNode(Cell(row,col),
									curr.dist+1)
				q.append(Adjcell)
	
	# Return -1 if destination cannot be reached 
	return -1

# Driver code
mat = [ [ 1, 0, 1, 1, 1 ],
	[ 1, 0, 1, 0, 1 ], 
	[ 1, 1, 1, 0, 1 ], 
	[ 0, 0, 0, 0, 1 ], 
	[ 1, 1, 1, 0, 1 ]]
source = Cell(0,0)
dest = Cell(2,1)
	
dist = bfsLee(mat,source,dest)
	
if dist!=-1:
		print("Length of the Shortest Path is",dist)
else:
		print("Shortest Path doesn't exist")
