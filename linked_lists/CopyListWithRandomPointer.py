# -*- coding: utf-8 -*-

"""
https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1229/
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.


Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.


Constraints:

-10000 <= Node.val <= 10000
Node.random is null or pointing to a node in the linked list.
Number of Nodes will not exceed 1000.
"""

import copy

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    """First solution using module Copy"""

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        ptr = head
        new_list = []
        while ptr:
            node = copy.deepcopy(ptr)
            new_list.append(node)
            ptr = ptr.next

        head = new_list[0]
        return head


class Solution2:
    """Second solution without any external modules"""

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        ptr = head
        new_list = []
        old_to_new = dict()
        while ptr:
            if ptr not in old_to_new:
                node = Node(ptr.val)
                old_to_new[ptr] = node
            else:
                node = old_to_new[ptr]

            if ptr.next:
                if ptr.next not in old_to_new:
                    next_node = Node(ptr.next.val)
                    old_to_new[ptr.next] = next_node
                else:
                    next_node = old_to_new[ptr.next]
                node.next = next_node
            if ptr.random:
                if ptr.random not in old_to_new:
                    random_node = Node(ptr.random.val)
                    old_to_new[ptr.random] = random_node
                else:
                    random_node = old_to_new[ptr.random]
                node.random = random_node

            new_list.append(node)
            ptr = ptr.next

        head = new_list[0]
        return head