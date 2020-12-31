import unittest
from bubble import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_sorted(self):
        _sorted = [1, 2, 3, 4]
        self.assertEqual(_sorted, bubble_sort(_sorted))
    def test_workflow(self):
        self.assertNotEqual(4,5)


    def test_bubble(self):
        unsorted = [4, 3, 2, 1, 12]
        _sorted = bubble_sort(unsorted)
        expected_results = [1, 2, 3, 4, 12]
        self.assertEqual(expected_results, _sorted)

if __name__ == '__main__':
    unittest.main()
