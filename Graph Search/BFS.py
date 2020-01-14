import math

from graph import Graph


def bfs(g, s):
    """
    Breadth first search algorithm
    :param g: Graph in adjancency list
    :param s: the start vertex
    """
    visited = [False] * len(g.graph)
    queue = [s]
    visited[s] = True

    while queue:
        v = queue.pop(0)
        print(v)

        for i in g.graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def augmented_bfs(g, s):
    visited = [False] * len(g.graph)
    l = [math.inf] * len(g.graph)
    l[s] = 0
    queue = [s]

    while queue:
        v = queue.pop(0)
        print(v)

        for i in g.graph[v]:
            if not visited[i]:
                visited[i] = True
                l[i] = l[v] + 1
                queue.append(i)


def main():
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    augmented_bfs(g, 2)


if __name__ == '__main__':
    main()
