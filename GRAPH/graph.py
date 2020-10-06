from random import randint
import toyplot
import toyplot.browser
import numpy
import random
import string


#! TODO:
# *Add support for directed graph
# *Modify show_graph() to support directed edges


class Graph:
    def __init__(self, undirected=True):
        # self.graph stores key-value pairs where the key is the vertex and
        self.graph = {}
        self.undirected = undirected

    # Add edge to graph (Sets, no duplicates)
    def add_edge(self, edge):
        # unpack the edge, src= starting vertex | dest = ending vertex
        src, dest = edge
        # if src exists we can add dest to the existing set, else add src as a key and initialize new set with dest as the value
        # undirected graphs cannot have loops or duplicate edges
        if self.undirected:
            if src != dest:
                if src in self.graph:
                    self.graph[src].add(dest)
                else:
                    self.graph[src] = {dest}
                # since the graph is undirected, we can add the relationship for dest-src in the same way we did src-dest above
                    if dest in self.graph:
                        self.graph[dest].add(src)
                    else:
                        self.graph[dest] = {src}
        else:
            # * Add directed graph code here
            pass

    # Add vertex to graph
    def add_vertex(self, v):
        # if the vertex v is not in the graph we add it and initialize the value as an empty set
        if v not in self.graph:
            self.graph[v] = set()
    # Return the edges of the undirected graph.

    def generate_edges(self):
        edges = set()
        for v1 in self.graph.keys():
            if not self.graph[v1]:
                edges.add((v1, v1))
            else:
                for v2 in self.graph[v1]:
                    # Check to see if the pair may have been added in reverse.
                    # No need to check for duplicates after, as a set wont allow an in-order duplicate edge
                    if (v2, v1) not in edges:
                        edges.add((v1, v2))

        print('edges:', edges)
        return edges

    def print_graph(self):
        print('graph:\n', self.graph)
    # region BFS
    # ^ Breadth First Search

    def BFS(self):
        print("\nBFS:")
        visited = {key: False for key in self.graph}
        start = next(iter(self.graph))
        q = [start]
        visited[start] = True

        while q:
            v = q.pop(0)
            print(v, end=' -> ') if False in visited.values(
            ) else print(v, end=' ')

            for n in self.graph[v]:
                if not visited[n]:
                    q.append(n)
                    visited[n] = True

        if False in visited.values():
            print("\nGraph disconnected. Vertices {} not reachable with BFS".format(
                [v for v in visited if not visited[v]]))

    # endregion
    # region DFS

    # ^ Depth First Search
    # 0. Create a dictionary called visited with all of the verticies as keys and set values as False
    # 1. Start at first vertex/key in our graph
    # 2. Pass the vertex to DFS. Mark as visited. Iterate through connected verticies
    # 2. Repeat for all unvisited verticies.

    def _DFS(self, v, visited):
        visited[v] = True
        # Check if all nodes are visited, if they are all True we remove arrow from print
        print(v, end=' -> ') if False in visited.values(
        ) else print(v, end=' ')
        for v2 in self.graph[v]:
            if not visited[v2]:
                self._DFS(v2, visited)

    def DFS(self):
        visited = {key: False for key in self.graph}
        start = next(iter(self.graph))
        print("DFS:")
        self._DFS(start, visited)
        if False in visited.values():
            print("\nGraph disconnected. Vertices {} not reachable with DFS".format(
                [v for v in visited if not visited[v]]))
    # endregion

    def gen_graph(self, letters=True, min=1, max=51):
        n_vertices = random.randrange(min, max)

        for i in range(n_vertices):
            if letters:
                self.add_edge((random.choice(string.ascii_uppercase),
                               random.choice(string.ascii_uppercase)))
            else:
                self.add_edge((random.choice(range(n_vertices)),
                               random.choice(range(n_vertices))))

        # self.add_edge()
    def n_vertices(self):
        return len(self.graph)


def show_graph(e):
    edges = numpy.array(
        list(e))
    layout = toyplot.layout.FruchtermanReingold()
    colormap = toyplot.color.brewer.map("Set2")
    vmax_size = 70
    canvas, axes, mark = toyplot.graph(
        edges,
        layout=layout,
        ewidth=3,
        eopacity=1,
        vcolor=colormap,
        vsize=vmax_size-graph.n_vertices(),
        width=1000,
    )

    toyplot.browser.show(canvas, "figure1.html")


if __name__ == "__main__":
    graph = Graph()

    #graph.gen_graph(letters=False, min=5, max=6)
    graph.graph = {3: {2}, 2: {3}, 1: {0}, 0: {1}}
    graph.print_graph()
    # e = graph.generate_edges()
    # show_graph(e)
    graph.DFS()
    graph.BFS()
