# -*- coding: utf-8 -*-
"""
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]


Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
Example 2:

Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.
Example 3:

Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.


Constraints:

2 <= arr.length <= 500
-10^3 <= arr[i] <= 10^3
"""

from typing import List


class Solution:
    """My solution"""
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if arr[i] == 2 * arr[j] or 2 * arr[i] == arr[j]:
                    return True


class Solution2:
    """Solution by a some smart man"""
    def checkIfExist(self, arr: List[int]) -> bool:
        d = {}
        for el in arr:
            if el * 2 in d or (el % 2 == 0 and el // 2 in d):
                return True
            d[el] = 1

        return False
