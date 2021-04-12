from enum import Enum

class Visit_Mode(Enum):
    VISITED = 1
    NOT_VISITED = 2

class Vectex:
    def __init__(self):
        self.data = None
        self.visited= None
        self.index= None
        self.next= None
        self.adjacency_list= None

class Edge:
    def __init__(self):
        self.weight = None
        self.next = None
        self.from_vertex = None
        self.target_vertex = None

class Graph:
    def __init__(self):
        self.vertex_count = None
        self.vertices = None

class ControlGraph:
    def create_graph(self):
    def destory_graph(self):
    def create_vertex(self, data):
        vertex = Vectex()
        vertex.data = data
        vertex.next = None
        vertex.adjacency_list = None
        vertex.visited = Visit_Mode.NOT_VISITED
        vertex.index = -1
    return vertex

    def destroy_vertex(self):
    def create_edge(self):
    def destroy_edge(self):
    def add_vertex(self, graph, vertex):
        

    def add_edge(self):

    def print_graph(self, graph):
        vertex = None
        edge = None
        if ((vertex = graph.vertices) == None):
            return
        
        while (vertex != None):
            print("{}".format(vertex.data), end=" ")

            if((edge = vertex.adjacency_list) == None):
                vertex = vertex.next
                print()
                continue

            while (edge != None):
                print("{}[{}]".format(edge.target_vertex.data, edge.weight))
                edge = edge.next
            
            print()
            vertex = vertex.next
        
        print()



if __name__ == "__main__":
    g = create_graph()
    vertex v1 = create_vertex('1')
