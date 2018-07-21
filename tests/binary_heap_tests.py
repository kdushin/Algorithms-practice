import unittest
import src.binary_heap


class TestHeapSort(unittest.TestCase):

    def test_heap_sort(self):
        heap = src.binary_heap.Heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
        heap.build_heap()
        heap.sort()
        self.assertEqual([1, 2, 3, 4, 7, 8, 9, 10, 14, 16], heap.Array)
