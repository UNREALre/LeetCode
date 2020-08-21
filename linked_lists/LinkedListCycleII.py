# -*- coding: utf-8 -*-
"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.


Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Follow-up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    This method is also dependent on Floyd’s Cycle detection algorithm.

    1. Detect Loop using Floyd’s Cycle detection algorithm and get the pointer to a loop node.
    2. Count the number of nodes in loop. Let the count be k.
    3. Fix one pointer to the head and another to a kth node from the head.
    4. Move both pointers at the same pace, they will meet at loop starting node.
    """
    def detectCycle(self, head: ListNode) -> ListNode:
        # 1. Detect if there is cycle
        slow_node = fast_node = head
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
            if slow_node == fast_node:
                break
        else:
            return None

        # 2. Here we can say, that cycle exists. Let's find out its length.
        cycle_length = 0
        while slow_node.next != fast_node:
            slow_node = slow_node.next
            cycle_length += 1

        # 3. Move slow to head and start to move both nodes by one node per iteration.
        # When they'll meat each other - we will find out our starting node
        slow_node = head
        while slow_node != fast_node:
            slow_node = slow_node.next
            fast_node = fast_node.next

        return slow_node