# -*- coding: utf-8 -*-
"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return l1

        l1_ptr = l1
        l2_ptr = l2
        self.sorted = []
        while l1_ptr or l2_ptr:
            if l1_ptr and l2_ptr:
                if l1_ptr.val <= l2_ptr.val:
                    self.add_to_sorted(l1_ptr.val)
                    l1_ptr = l1_ptr.next
                else:
                    self.add_to_sorted(l2_ptr.val)
                    l2_ptr = l2_ptr.next
            elif l1_ptr:
                self.add_to_sorted(l1_ptr.val)
                l1_ptr = l1_ptr.next
            else:
                self.add_to_sorted(l2_ptr.val)
                l2_ptr = l2_ptr.next

        return self.sorted

    def add_to_sorted(self, val: int) -> None:
        print(val)
        new_node = ListNode(val)
        if not self.sorted:
            self.sorted = new_node
        else:
            tail = self.sorted
            while tail.next:
                tail = tail.next
            tail.next = new_node
