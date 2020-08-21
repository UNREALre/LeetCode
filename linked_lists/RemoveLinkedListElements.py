# -*- coding: utf-8 -*-
"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        cur_node = head
        prev_node = None
        while cur_node:
            if cur_node.val == val:
                if prev_node:
                    prev_node.next = cur_node.next
                else:
                    head = cur_node.next
            else:
                prev_node = cur_node

            cur_node = cur_node.next

        return head
