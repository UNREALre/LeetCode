# -*- coding: utf-8 -*-
"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

from typing import List


class Solution:
    """My Solution"""
    def removeDuplicates(self, nums: List[int]) -> int:
        deleted = 0
        for i in range(len(nums) - deleted - 1):
            equal_num = 0
            j = i + 1
            while j < len(nums) - deleted and nums[j] == nums[i]:
                equal_num += 1
                j += 1
            if j == len(nums):
                deleted += equal_num
                break
            if equal_num:
                for k in range(j, len(nums) - deleted):
                    nums[k - equal_num] = nums[k]
                deleted += equal_num

        return len(nums) - deleted


class Solution2:
    """
    Cool solution from other man... Wish I've code this by myself
    [!] two-pointer technique
    """
    def removeDuplicates(self, l: List[int]) -> int:
        pos = 0
        for n in l:
            if n != l[pos]:
                pos += 1
                l[pos] = n
        return pos + 1


class Solution3:
    """
    My solution after couple of days in the task where I was asked to
    create algorith with complexity = O(N)
    [!] two-pointer technique
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        deleted = 0
        index = 0
        cur_index = 1
        while cur_index < len(nums):
            if nums[cur_index] == nums[index]:
                deleted += 1
            else:
                nums[index + 1] = nums[cur_index]
                index += 1

            cur_index += 1

        return len(nums) - deleted
