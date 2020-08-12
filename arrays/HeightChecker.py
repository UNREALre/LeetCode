# -*- coding: utf-8 -*-
"""
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.

Notice that when a group of students is selected they can reorder in any possible way between themselves and the non selected students remain on their seats.



Example 1:

Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation:
Current array : [1,1,4,2,1,3]
Target array  : [1,1,1,2,3,4]
On index 2 (0-based) we have 4 vs 1 so we have to move this student.
On index 4 (0-based) we have 1 vs 3 so we have to move this student.
On index 5 (0-based) we have 3 vs 4 so we have to move this student.
Example 2:

Input: heights = [5,1,2,3,4]
Output: 5
Example 3:

Input: heights = [1,2,3,4,5]
Output: 0


Constraints:

1 <= heights.length <= 100
1 <= heights[i] <= 100
"""

from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        write_pointer = 0
        default = heights.copy()
        while write_pointer < len(heights):
            read_pointer = len(heights) - 1
            while read_pointer > write_pointer:
                if heights[read_pointer] < heights[write_pointer]:
                    heights[read_pointer], heights[write_pointer] = heights[write_pointer], heights[read_pointer]
                    break
                else:
                    read_pointer -= 1
            if write_pointer == read_pointer:
                write_pointer += 1

        changes = 0
        for idx, elem in enumerate(default):
            if elem != heights[idx]:
                changes += 1

        return changes


class Solution2:
    def heightChecker(self, heights: List[int]) -> int:
        s_heights = sorted(heights)
        changes = 0
        for idx, elem in enumerate(heights):
            if elem != s_heights[idx]:
                changes += 1

        return changes
    