class Graph:
    def __init__(self,vertex):
        self.mat = [[0]*vertex for x in range(vertex)]
        self.size = vertex
#for undirected graph
    def add_edge(self,src,dest,weight):
        if 0<= src <self.size and 0< dest <self.size:
            self.mat[src][dest] = weight
            self.mat[dest][src] = weight #optional if use undirected graph
# for the weighted graph
        # def add_edge(self,src,dest,weight):
        #     if 0<= src <self.size and 0< dest <self.size:
        #         self.mat[src][dest] = weight
        #         self.mat[dest][src] = weight #optional if use undirected graph
        #     else:
        #         print("Invalid edge")
        else:
            print("invalid edge")
#print function
    def print(self):
        for row in self.mat:
            print(" ".join(map(str,row)))

#call the function
my_graph = Graph(5)
# G.add_edge(0,1)
# G.add_edge(0,2)
# G.add_edge(1,3)
# G.add_edge(2,4)
# G.add_edge(3,4)
# G.add_edge(2,4)
my_graph.add_edge(0,1,5)
my_graph.add_edge(0,2,6)
my_graph.add_edge(1,3,7)
my_graph.add_edge(2,3,5)
my_graph.add_edge(2,4,6)
my_graph.add_edge(3,4,9)
my_graph.print()