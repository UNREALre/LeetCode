# -*- coding: utf-8 -*-

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr1 = l1
        ptr2 = l2
        num1 = num2 = ""
        while ptr1 or ptr2:
            if ptr1:
                num1 += str(ptr1.val)
                ptr1 = ptr1.next
            if ptr2:
                num2 += str(ptr2.val)
                ptr2 = ptr2.next

        num1 = int(num1[::-1])
        num2 = int(num2[::-1])
        num3 = str(num1 + num2)[::-1]

        new_list = None
        for number in num3:
            new_node = ListNode(number)
            if not new_list:
                new_list = new_node
            else:
                tail = new_list
                while tail.next:
                    tail = tail.next
                tail.next = new_node

        return new_list
