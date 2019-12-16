import unittest
from Divide_and_Conquer.counting_inversions import sort_and_count_inv
from tests.base import TestAlgorithm


class TestDivideAndConquer(TestAlgorithm):
    def test_counting_inv(self):
        case1 = [1, 3, 5, 2, 4, 6]
        expect_1 = 3
        _, inv_n_1 = sort_and_count_inv(case1)
        self.assertEqual(inv_n_1, expect_1,
                         self.MESSAGE_TPL.format(case1, expect_1,
                                                 inv_n_1))
        case2 = [1, 5, 3, 2, 4]
        expect_2 = 4
        _, inv_n_2 = sort_and_count_inv(case2)
        self.assertEqual(inv_n_2, expect_2,
                         self.MESSAGE_TPL.format(case2, expect_2,
                                                 inv_n_2))
        case3 = [5, 4, 3, 2, 1]
        expect_3 = 10
        _, inv_n_3 = sort_and_count_inv(case3)
        self.assertEqual(inv_n_3, expect_3,
                         self.MESSAGE_TPL.format(case3, expect_3,
                                                 inv_n_3))


if __name__ == '__main__':
    unittest.main()
