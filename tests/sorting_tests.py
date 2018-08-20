import unittest
from src.Sorting import linear_sorting


class TestSorting(unittest.TestCase):

    def test_counting_sort(self):
        sorted_array = linear_sorting.counting_sort([4, 1, 3, 2, 16, 9, 10, 14, 8, 7, 9], 16)
        self.assertEqual([1, 2, 3, 4, 7, 8, 9, 9, 10, 14, 16], sorted_array)
