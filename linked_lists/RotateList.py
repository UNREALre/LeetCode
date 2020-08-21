# -*- coding: utf-8 -*-

"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head

        rotated = [None]
        list_size = 1
        ptr = head
        while ptr.next:
            list_size += 1
            ptr = ptr.next
            rotated.append(None)

        # If we are asked to move list to the number k which % on list_size = 0 - list placement will be the same
        if k % list_size == 0:
            return head

        ptr = head
        cur_index = 0
        while ptr:
            new_index = (cur_index + k) % list_size
            rotated[new_index] = ListNode(ptr.val)
            ptr = ptr.next
            cur_index += 1

        for i in range(list_size - 1):
            rotated[i].next = rotated[i + 1]

        head = rotated[0]
        return head
