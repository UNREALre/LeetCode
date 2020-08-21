# -*- coding: utf-8 -*-
"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up:

Can you solve it using O(1) (i.e. constant) memory?
"""

from typing import List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    First approach solution.

    This one and next solution based on idea that if one pointer will be at node X and other one at node
    X+2, we will be able to find out cycle at one of iterations or we will get to the end of the list.
    We know that Floyd’s Cycle detection algorithm terminates when fast and slow
    pointers meet at a common point.
    """
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        elif head == head.next:
            return True
        elif not head.next.next:
            return False
        elif head.next.next == head.next or head.next.next == head:
            return True
        else:
            slow_node = head
            fast_node = head.next.next
            while fast_node:
                if slow_node == fast_node:
                    break
                try:
                    slow_node = slow_node.next
                    fast_node = fast_node.next.next
                except AttributeError:
                    return False
            else:
                return False

            return True


class Solution2:
    """Second approach solution. Clean & simple Floyd's cycle detection."""
    def hasCycle(self, head: ListNode) -> bool:
        slow_node = fast_node = head
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
            if slow_node == fast_node:
                break
        else:
            return False

        return True
