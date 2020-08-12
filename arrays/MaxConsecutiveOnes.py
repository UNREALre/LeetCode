# -*- coding: utf-8 -*-
"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = counter = 0
        for elem in nums:
            if elem == 1:
                counter += 1
                if max_num < counter:
                    max_num = counter
            else:
                counter = 0

        return max_num
