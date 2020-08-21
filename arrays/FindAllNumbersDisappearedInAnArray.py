# -*- coding: utf-8 -*-
"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

from typing import List


class Solution:
    """First approach solution with complexity O(N^2), and we are asked for compl. = O(N)"""
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        rez = []
        for i in range(1, len(nums) + 1):
            found = False
            for elem in nums:
                if elem == i:
                    found = True
                    break
            if not found:
                rez.append(i)

        return rez


class Solution2:
    """Second approach. Now with complexity = O(N). Runtime beats 83.94% submissions"""
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        rez = [None for i in range(len(nums))]
        for elem in nums:
            rez[elem-1] = 1
        return [idx+1 for idx, elem in enumerate(rez) if elem == None]


class Solution3:
    """
    Third approach with no additional memory used.
    I guess complexity O(N), but runtime worser than before: 53.95%
    """
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if (nums[index] > 0):
                nums[index] = -nums[index]
        return [idx+1 for idx, elem in enumerate(nums) if elem > 0]
