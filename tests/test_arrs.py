import unittest
from arrs import get
from arrs import my_slice


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(get([1, 2, 3], -1, "test"), "test")

    def test_my_slice(self):
        self.assertEqual(my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(my_slice([], 1), [])

        self.assertEqual(my_slice([1, 2, 3], -7), [1, 2, 3])
        self.assertEqual(my_slice([1, 2, 3, 4, 5], -3), [3, 4, 5])






