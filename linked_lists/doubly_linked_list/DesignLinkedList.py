# -*- coding: utf-8 -*-

"""
Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
addAtTail(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.

Example:

Input:
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1]]
Output:
[null,null,null,null,2,null,3]

Explanation:
MyLinkedList linkedList = new MyLinkedList(); // Initialize empty LinkedList
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3


Constraints:

0 <= index,val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail,  addAtIndex and deleteAtIndex.
"""


class Node:
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node

    def get_prev(self):
        return self.prev_node

    def set_prev(self, prev_node):
        self.prev_node = prev_node


class MyLinkedList:

    def __init__(self, head=None):
        """Initialize your data structure here."""
        self.head = head

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()

        return count

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < self.size():
            current_index = 0
            node = self.head
            while current_index < index:
                current_index += 1
                node = node.get_next()
            return node.get_data()

        return -1

    def search(self, index: int) -> Node:
        """Search the node by index"""
        current_index = 0
        node = self.head
        while current_index < index:
            current_index += 1
            node = node.get_next()

        return node if current_index == index else None

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val, self.head)
        if self.head:
            self.head.set_prev(new_node)
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        list_size = self.size()
        if list_size:
            last_node = self.search(list_size - 1)
            new_node = Node(val, prev_node=last_node)
            last_node.set_next(new_node)
        else:
            self.addAtHead(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
         If index is greater than the length, the node will not be inserted.
        """
        if index <= self.size():
            node = self.search(index)
            if not node:
                self.addAtTail(val)
            elif self.head == node:
                self.addAtHead(val)
            else:
                prev_node = node.get_prev()
                new_node = Node(val, node, prev_node)
                prev_node.set_next(new_node)
                node.set_prev(new_node)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self.head = self.head.get_next()
        elif index < self.size():
            node = self.search(index)
            prev_node = node.get_prev()
            next_node = node.get_next()

            prev_node.set_next(next_node)
            if next_node:
                next_node.set_prev(prev_node)
