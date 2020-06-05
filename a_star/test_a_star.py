from unittest import TestCase

from a_star import calc_dist, get_path, shortest_path
from helper import load_map


class Test(TestCase):
    def test_get_path(self):
        test_case = (({1: 0, 2: 1, 3: 2, 4: 3}, 0, 4), [0, 1, 2, 3, 4])
        self.assertEqual(get_path(*test_case[0]), test_case[1])

    def test_shortest_path(self):
        map_40 = load_map('map-40.pickle')
        test_cases = [
            (5, 34, [5, 16, 37, 12, 34]),
            (5, 5, [5]),
            (8, 24, [8, 14, 16, 37, 12, 17, 10, 24])
        ]
        for test_case in test_cases:
            self.assertEqual(shortest_path(map_40, *test_case[:2]), test_case[-1])

