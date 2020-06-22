from unittest import TestCase
from sorting_algos.quicksort import quick_sort


class Test(TestCase):
    def test_quick_sort(self):
        self.assertEqual(quick_sort([]), [])
        self.assertEqual(quick_sort([1]), [1])
        self.assertEqual(quick_sort([3, 4, 5, 7, 8, 1, 2]), [1, 2, 3, 4, 5, 7, 8])
