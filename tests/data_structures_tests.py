import unittest
from src.DataStructures import stack


class TestDataStructure(unittest.TestCase):

    def test_stack(self):
        arr = [1, 3]
        stack.Stack.push(arr, 4)
        self.assertEqual([1, 3, 4], arr)
        stack.Stack.pop(arr)
        self.assertEqual([1,3], arr)
        stack.Stack.pop(arr)
        self.assertEqual([1], arr)
        try:
            stack.Stack.pop(arr)
        except AssertionError as ae:
            return
        self.fail("Stack overflow exception wasn't raised")