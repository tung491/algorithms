from unittest import TestCase
from sorting_algos.selection_sort import selection_sort

class Test(TestCase):
    def test_selection_sort(self):
        self.assertEqual(selection_sort([]), [])
        self.assertEqual(selection_sort([1]), [1])
        self.assertEqual(selection_sort([4, 3, 6, 8, 1, 5]), [1, 3, 4, 5, 6, 8])
