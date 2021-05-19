"""
    Bubble Sort
    Steps:
        1. Loop through the list.
        2. Compare the next element with current element.
        3. Swap both element if first value of first element is larger.
        4. Recursive call the sort function.
"""

import numpy as np
import unittest

class BubbleSort:
    def bubble_sort(self, arr):
        length = len(arr)
        for i in range(length-1):
            j = i+1
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            
        if length > 1:
            self.bubble_sort(arr[0:length-1])

class Testing(unittest.TestCase):
    def setUp(self):
        self.bSort = BubbleSort()

    def test_basic_sorting(self):
        arr = np.array([2,3,1,4,0])
        sorted_arr = np.array([0,1,2,3,4])
        self.bSort.bubble_sort(arr)
        np.testing.assert_array_equal(sorted_arr, arr)

if __name__ == '__main__':
    unittest.main()
