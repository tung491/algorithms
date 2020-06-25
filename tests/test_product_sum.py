from unittest import TestCase
from problems.product_sum import product_sum


class Test(TestCase):
    def test_product_sum(self):
        self.assertEqual(product_sum([1, 2, [3, 4]]), 17)
        self.assertEqual(product_sum([]), 0)
