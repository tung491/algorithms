from unittest import TestCase
from sorting_algos.insertion_sort import insertion_sort

class Test(TestCase):
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([]), [])
        self.assertEqual(insertion_sort([1]), [1])
        self.assertEqual(insertion_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(insertion_sort([1, 3, 2, 4, 5, 8, 7]), [1, 2, 3, 4, 5, 7, 8])
