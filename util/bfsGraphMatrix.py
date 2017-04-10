from c_graph import graphMatrix
from c_queue import queueADT

def bfs(G,root):
    que=queueADT.Queue()
    visited = {}
    initial=True
    if(initial):
        que.enQueue(root)
        bfsTraversal(G,visited,que)
        initial=False

    for x in range(G.numVertices):
        if(x not in visited):
            que.enQueue(x)
            bfsTraversal(G,visited,que)



def bfsTraversal(G,visited,que):
    if(que.size==0):
        return
    else:
        visitNode = que.deQueue()
        print(visitNode, end=" ")
        visited[visitNode]=True
        for neighbour in G.getNeighbour(visitNode):
            if neighbour not in visited:
                que.enQueue(neighbour)
        bfsTraversal(G,visited,que)




if __name__=="__main__":
    G=graphMatrix.Graph(4)
    G.addEdge(0,1,1,0)
    G.addEdge(1,2,1,0)
    G.addEdge(2,3,1,0)
    G.addEdge(0,3,1,0)
    G.addEdge(2,0,1,0)
    G.print()
    bfs(G,0)
