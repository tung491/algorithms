from unittest import TestCase
from sorting_algos.bubble_sort import bubble_sort


class Test(TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([1]), [1])
        self.assertEqual(bubble_sort([1, 3, 4, 2, 6, 9]), [1, 2, 3, 4, 6, 9])
