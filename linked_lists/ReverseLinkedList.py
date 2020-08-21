# -*- coding: utf-8 -*-
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

from typing import List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        cur_node = head.next
        prev_node = head
        while cur_node:
            prev_node.next = cur_node.next
            cur_node.next = head
            head = cur_node
            cur_node = prev_node.next

        return head


class Solution2:
    """Version with recursion"""
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        self.head = head
        self.reverse(head, head.next)

        return self.head

    def reverse(self, prev_node, cur_node):
        prev_node.next = cur_node.next
        cur_node.next = self.head
        self.head = cur_node
        cur_node = prev_node.next
        if cur_node:
            self.reverse(prev_node, cur_node)
