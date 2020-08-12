# -*- coding: utf-8 -*-
"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        read_pointer = 0
        write_pointer = 0
        while read_pointer < len(nums):
            if nums[write_pointer] != 0:
                write_pointer += 1
            elif nums[read_pointer] != 0:
                nums[write_pointer], nums[read_pointer] = nums[read_pointer], nums[write_pointer]
                write_pointer += 1
            read_pointer += 1

        return nums
