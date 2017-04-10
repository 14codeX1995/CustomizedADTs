from c_graph import graphMatrix


def dfs(G,root):
    visited={}
    initial=True
    if(initial):
        dfsTraversal(G,root,visited)
        initial=False
    for x in range(G.numVertices):
        if(x not in visited):
            dfsTraversal(G,x,visited)

def dfsTraversal(G,x,visited):
    visited[x]=True
    print(x,end=" ")
    for i in G.getNeighbour(x):
        if(i not in visited):
            dfsTraversal(G,i,visited)

if __name__=="__main__":
    G=graphMatrix.Graph(4)
    G.addEdge(0,1,1,0)
    G.addEdge(1,2,1,0)
    G.addEdge(2,3,1,0)
    G.addEdge(0,3,1,0)
    G.addEdge(2,0,1,0)
    G.print()
    dfs(G,0)




