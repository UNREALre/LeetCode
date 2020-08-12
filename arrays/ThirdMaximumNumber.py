# -*- coding: utf-8 -*-
"""

"""

from typing import List
import math


class Solution:
    """
    First approach decision. I don't like it, cause IMHO it's unreadable...
    BUT: if the task is not to use external libs (like maths, sys etc) - seems it's the only way
    to solve this task with complexity O(N), when we have to say that max2 and 3 equals None, not -inf.
    Below is a solution with -math.inf
    """
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            if len(nums) == 2:
                max = nums[0] if nums[0] > nums[1] else nums[1]
            else:
                max = nums[0]

            return max

        max1 = nums[0]
        max2 = max3 = None
        for i in range(1, len(nums)):
            if max1 < nums[i]:
                max3, max2, max1 = max2, max1, nums[i]
            elif not max2 and nums[i] != max1:
                max2 = nums[i]
            elif max2 and nums[i] != max1 and max2 < nums[i]:
                max3, max2 = max2, nums[i]
            elif not max3 and nums[i] != max1 and nums[i] != max2:
                max3 = nums[i]
            elif max3 and nums[i] != max1 and nums[i] != max2 and max3 < nums[i]:
                max3 = nums[i]

        return max3 if max3 != None else max1


class Solution2:
    """
    The same idea of algorithm as within previous solution, BUT now we use -math.inf for min values,
    and our code is more readable.
    """
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            if len(nums) == 2:
                max = nums[0] if nums[0] > nums[1] else nums[1]
            else:
                max = nums[0]

            return max

        max1 = max2 = max3 = -math.inf
        for elem in nums:
            if elem >= max1:
                if elem > max1:
                    max3, max2, max1 = max2, max1, elem
            elif elem >= max2:
                if elem > max2:
                    max3, max2 = max2, elem
            elif elem > max3:
                max3 = elem

        return max3 if max3 != -math.inf else max1
