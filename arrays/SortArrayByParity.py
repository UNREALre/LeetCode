# -*- coding: utf-8 -*-
"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.



Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
"""

from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        read_pointer = len(A) - 1
        write_pointer = 0
        while read_pointer >= 0 and read_pointer > write_pointer:
            if A[read_pointer] % 2 == 0:
                if A[write_pointer] % 2 != 0:
                    A[write_pointer], A[read_pointer] = A[read_pointer], A[write_pointer]
                    read_pointer -= 1
                write_pointer += 1
            else:
                read_pointer -= 1

        return A
