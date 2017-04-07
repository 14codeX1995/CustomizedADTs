class Graph:
    def __init__(self,numVertices):
        self.adjMatrix=[[0]*4 for _ in range(numVertices)]
        self.numVertices=numVertices

    def addEdge(self,frm, to, wt,undirected=1):
        self.adjMatrix[frm][to]=wt
        if(undirected):
            self.adjMatrix[to][frm]=wt

    def print(self):
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                if(self.adjMatrix[i][j]!=0):
                    print(i,"->",j,":",self.adjMatrix[i][j])

    def getNeighbour(self,x):
        neighbour=[]
        for i in range(self.numVertices):
            if(self.adjMatrix[x][i]==1):
                neighbour.append(i)
        return neighbour
