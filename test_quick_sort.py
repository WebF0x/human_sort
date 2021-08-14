import unittest

from quick_sort import quick_sort


def is_smaller(a, b):
    return a < b


class QuickSortTest(unittest.TestCase):
    def test_sort_nothing(self):
        self.assertEqual([], quick_sort([], is_smaller))

    def test_sort_single_thing(self):
        self.assertEqual([42], quick_sort([42], is_smaller))

    def test_sort_sorted_things(self):
        self.assertEqual([1, 2, 3], quick_sort([1, 2, 3], is_smaller))

    def test_sort_unsorted_things(self):
        self.assertEqual([1, 2, 3], quick_sort([3, 2, 1], is_smaller))

    def test_sort_duplicated_things(self):
        self.assertEqual([1, 2, 2, 3], quick_sort([2, 3, 2, 1], is_smaller))

    def test_sort_with_custom_compare_function(self):
        def is_bigger(a, b):
            return b < a
        self.assertEqual([4, 3, 2, 1], quick_sort([1, 2, 3, 4], is_bigger))


if __name__ == '__main__':
    unittest.main()
