# -*- coding: utf-8 -*-
"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.



Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]


Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
"""

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if arr:
            if len(arr) > 2:
                max = arr[-1]
                arr[-1] = -1
                for i in range(len(arr) - 2, -1, -1):
                    cur_elem = arr[i]
                    arr[i] = max
                    if max < cur_elem:
                        max = cur_elem
            elif len(arr) == 2:
                arr[0] = arr[1]
                arr[1] = -1
            else:
                arr[0] = -1

        return arr
