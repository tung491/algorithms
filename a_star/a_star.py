import math
from typing import Union
import sys

from helper import load_map, Map

sys.path.insert(0, '..')
from data_structure.heap import MinHeap


def calc_dist(point1: list, point2: list) -> float:
    x1, y1 = point1
    x2, y2 = point2
    difference_x = x2 - x1
    difference_y = y2 - y1
    return math.sqrt(pow(difference_x, 2) + pow(difference_y, 2))


def get_path(previous: dict, start: int, goal: int) -> list:
    path = [start, goal]
    node = previous[goal]
    while node != start:
        path.insert(1, node)
        node = previous[node]
    return path


def shortest_path(map_, start: int, goal: int) -> Union[list, None]:
    def get_intersect(road_i):
        return map_.intersections[road_i]

    frontiers = MinHeap()
    explored = set()
    score = {start: 0}
    previous_road = {}

    if start == goal:
        return [start]

    for road in map_.roads[start]:
        road_len = calc_dist(get_intersect(start), get_intersect(road))
        total_est_dist = score[start] + road_len
        score[road] = road_len
        frontiers.insert((total_est_dist, road))
        previous_road[road] = start

    while frontiers.heap:
        _, current = frontiers.extract_min()
        explored.add(current)
        if current == goal:
            return get_path(previous_road, start, goal)
        for node in map_.roads[current]:
            updated_score = score[current] + calc_dist(get_intersect(current),
                                                       get_intersect(node))
            if node not in score or updated_score < score[node]:
                score[node] = updated_score
                total_score = updated_score + calc_dist(get_intersect(node),
                                                        get_intersect(goal))
                frontiers.insert((total_score, node))
                previous_road[node] = current
    return None


def main() -> None:
    map_40 = load_map('map-40.pickle')
    path = shortest_path(map_40, 8, 24)
    print(path)


if __name__ == '__main__':
    main()
