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
        if src in self.graph:
            self.graph[src].add(dest)
        else:
            self.graph[src] = {dest}
        # since the graph is undirected, we can add the relationship for dest-src in the same way we did src-dest above
        if self.undirected:
            if dest in self.graph:
                self.graph[dest].add(src)
            else:
                self.graph[dest] = {src}

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

    def BFS(self):
        pass

    def DFS(self):
        visited = [False] * len(self.graph)
        start = next(iter(self.graph))

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


def show_graph():
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

    graph.gen_graph(letters=False, min=10, max=11)
    graph.print_graph()
    e = graph.generate_edges()
    # show_graph()
    graph.DFS()
