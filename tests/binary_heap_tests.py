import unittest
from src import binary_heap


class TestHeapSort(unittest.TestCase):

    def test_heap_sort(self):
        heap = binary_heap.Heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
        heap.build_heap()
        heap.sort()
        self.assertEqual([1, 2, 3, 4, 7, 8, 9, 10, 14, 16], heap.Array)

    def test_priority_queue_max_insert(self):
        heap = binary_heap.Heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
        heap.build_heap()
        heap.max_insert(15)
        self.assertEqual([16, 15, 10, 8, 14, 9, 3, 2, 4, 1, 7], heap.Array)

    def test_priority_queue_increase_key(self):
        heap = binary_heap.Heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
        heap.build_heap()
        self.assertEqual([16, 14, 10, 8, 7, 9, 3, 2, 4, 1], heap.Array)
        heap.increase_key(9, 15)
        self.assertEqual([16, 15, 10, 14, 7, 9, 3, 2, 8, 1], heap.Array)
