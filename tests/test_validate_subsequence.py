from unittest import TestCase
from problems.validate_subsequence import validate_subsequence


class Test(TestCase):
    def test_validate_subsequence(self):
        self.assertEqual(validate_subsequence([], []), True)
        self.assertEqual(validate_subsequence([1], [1]), True)
        self.assertEqual(validate_subsequence(list(range(10)), [1, 3, 5, 7]), True)
        self.assertEqual(validate_subsequence(list(range(10)), [3, 1]), False)
        self.assertEqual(validate_subsequence(list(range(10)), [3, 44]), False)
