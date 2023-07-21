import unittest
from merge_sort import merge_sort
from quick_sort import quick_sort
from tim_sort import tim_sort

class TestSortingAlgorithms(unittest.TestCase):
    def test_sort_algorithm(self, sort_function):
        self.assertEqual(sort_function([5, 2, 3, 1]), [1, 2, 3, 5])
        self.assertEqual(sort_function([5, 1, 1, 2, 0, 0]), [0, 0, 1, 1, 2, 5])
        self.assertEqual(sort_function([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(sort_function([1]), [1])
        self.assertEqual(sort_function([0]), [0])
        self.assertEqual(sort_function(list(range(10000, 0, -1)), list(range(1, 10001))))


    def test_quick_sort(self):
        self.test_sort_algorithm(quick_sort)

    def test_tim_sort(self):
        self.test_sort_algorithm(tim_sort)

    def test_merge_sort(self):
        self.test_sort_algorithm(merge_sort)

if __name__ == '__main__':
    unittest.main()