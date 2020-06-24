from unittest import TestCase
from problems.two_number_sum import unsorted_two_number_sum,\
    sorted_two_number_sum


class Test(TestCase):
    def test_sorted_two_number_sum(self):
        self.assertEqual(sorted_two_number_sum([1, 3], 2), [])
        self.assertEqual(sorted_two_number_sum([1, 5, 7, 8], 8), [1, 7])

    def test_unsorted_two_number_sum(self):
        self.assertEqual(unsorted_two_number_sum([1, 6, 4, 3, 8, 9, 22], 10), [1, 9])
        self.assertEqual(unsorted_two_number_sum([1, 2], 5), [])

