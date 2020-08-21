# -*- coding: utf-8 -*-

"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        # 1. Getting the size of list
        list_size = 1
        cur_node = head
        while cur_node.next:
            cur_node = cur_node.next
            list_size += 1

        # 2. Moving pointer 2 to the middle of list, while reversing first part of the list
        cur_index = 0
        ptr2 = head
        while cur_index < list_size // 2:
            ptr2 = ptr2.next
            cur_index += 1

        # 3. Reversing first part of the list
        if list_size > 3:
            ptr1 = head.next
            prev = head
            change_index = 1
            while change_index < list_size // 2:
                prev.next = ptr1.next
                ptr1.next = head
                head = ptr1
                change_index += 1
                ptr1 = prev.next

        # 4. If list size is odd, move second pointer to the next element before comparison process
        if list_size % 2 != 0:
            ptr2 = ptr2.next

        # 5. Checking two pointers - one at the head, second - at the middle. If nodes are equal? If not - break
        cur_index = 0
        ptr1 = head
        while cur_index < list_size // 2:
            print('{} - {}'.format(ptr1.val, ptr2.val))
            if ptr1.val != ptr2.val:
                break
            ptr1, ptr2 = ptr1.next, ptr2.next
            cur_index += 1
        else:
            return True

        return False
