# -*- coding: utf-8 -*-
"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.



Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""

from typing import List


class Solution:
    """First version without sorting function"""
    def sortedSquares(self, A: List[int]) -> List[int]:
        rez = []
        non_positive_squares = []
        for elem in A:
            square = elem * elem
            if elem <= 0:
                non_positive_squares.insert(0, square)
            elif non_positive_squares:
                if square < non_positive_squares[0]:
                    rez.append(square)
                else:
                    while non_positive_squares and non_positive_squares[0] <= square:
                        rez.append(non_positive_squares[0])
                        del (non_positive_squares[0])
                    rez.append(square)

            else:
                rez.append(square)

        while non_positive_squares:
            rez.append(non_positive_squares[0])
            del (non_positive_squares[0])

        return rez


class Solution2:
    """Using sorted"""
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([x*x for x in A])


class Solution3:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i in range(len(A)):
            A[i] = A[i] * A[i]

        for j in range(len(A)):
            i = 0
            while i < len(A) - 1 - j:
                if A[i] > A[i + 1]:
                    A[i + 1], A[i] = A[i], A[i + 1]
                i += 1

        return A
