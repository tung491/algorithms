from unittest import TestCase
from sorting_algos.merge_sort import merge_sort


class Test(TestCase):
    def test_merge_sort(self):
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort([1]), [1])
        self.assertEqual(merge_sort([1, 4, 3, 7, 4]), [1, 3, 4, 4, 7])
