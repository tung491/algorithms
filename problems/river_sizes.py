from typing import List

Matrix = List[List[int]]


def river_sizes(matrix: Matrix) -> List[int]:
    sizes = []
    visited = [[False for _ in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverse_node(i, j, matrix, visited, sizes)
    return sorted(sizes)


def traverse_node(i: int, j: int, matrix: Matrix, visited: List[List[bool]], sizes: List[int]):
    current_size = 0
    nodes_to_explore = [[i, j]]
    while nodes_to_explore:
        curr_node = nodes_to_explore.pop()
        i, j = curr_node
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        current_size += 1
        unvisited_neighbours = get_unvisited_neighbors(i, j, matrix, visited)
        for neighbor in unvisited_neighbours:
            nodes_to_explore.append(neighbor)
    if current_size > 0:
        sizes.append(current_size)


def get_unvisited_neighbors(i: int, j: int, matrix: Matrix, visited: List[List[bool]]):
    unvisited_neighbours = []
    if i > 0 and not visited[i - 1][j]:
        unvisited_neighbours.append((i - 1, j))
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisited_neighbours.append((i + 1, j))
    if j > 0 and not visited[i][j - 1]:
        unvisited_neighbours.append((i, j - 1))
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisited_neighbours.append((i, j + 1))
    return unvisited_neighbours


def test():
    matrix = [[1, 0, 0, 1, 0],
              [1, 0, 1, 0, 0],
              [0, 0, 1, 0, 1],
              [1, 0, 1, 0, 1],
              [1, 0, 1, 1, 0]]
    print(river_sizes(matrix))


if __name__ == '__main__':
    test()
