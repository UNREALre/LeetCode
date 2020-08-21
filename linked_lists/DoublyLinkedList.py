# -*- coding: utf-8 -*-
"""
Practising with linked list realization. Now - doubly linked list (with prev and next links)
"""

import sys


class Node:
    def __init__(self, data=None, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def __repr__(self):
        prev_val = self.get_prev().get_data() if self.get_prev() else None
        next_val = self.get_next().get_data() if self.get_next() else None
        return '<Node #{} data={}, prev_val={}, next_val={}>'.format(id(self), self.data, prev_val, next_val)

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def get_prev(self):
        return self.prev_node

    def set_data(self, data):
        self.data = data

    def set_next(self, node):
        self.next_node = node

    def set_prev(self, node):
        self.prev_node = node


class MyDoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        list = []
        cur_index = 0
        cur_object = self.head
        while cur_index < self.get_size():
            list.append(cur_object.get_data())
            cur_object = cur_object.get_next()
            cur_index += 1
        return '<MyDoublyList: {}>'.format('; '.join([str(elem) for elem in list]))

    def get_size(self):
        size = 0
        cur_node = self.head
        while cur_node:
            cur_node = cur_node.get_next()
            size += 1
        return size

    def get(self, index):
        node = None
        if index < self.get_size():
            cur_index = 0
            cur_node = self.head
            while cur_index < index:
                cur_node = cur_node.get_next()
                cur_index += 1
            node = cur_node
        return node

    def add_to_head(self, data):
        new_node = Node(data)
        if self.get_size():
            new_node.set_next(self.head)
            self.head.set_prev(new_node)

        self.head = new_node

    def add_to_tail(self, data):
        list_size = self.get_size()
        if list_size:
            tail = self.get(list_size-1)
            new_node = Node(data, tail)
            tail.set_next(new_node)
        else:
            self.add_to_head(data)

    def add(self, data, index):
        list_size = self.get_size()
        if index <= list_size:
            if index == 0:
                self.add_to_head(data)
            elif index == list_size:
                self.add_to_tail(data)
            else:
                node = self.get(index)
                prev_node = node.get_prev()
                new_node = Node(data, prev_node, node)
                prev_node.set_next(new_node)
                node.set_prev(new_node)

    def delete_node(self, index):
        if index < self.get_size():
            node = self.get(index)
            prev_node = node.get_prev()
            next_node = node.get_next()

            if prev_node:
                prev_node.set_next(next_node)
            else:
                self.head = next_node
            if next_node:
                next_node.set_prev(prev_node)

            node.set_prev(None)
            node.set_next(None)


dl = MyDoublyLinkedList()

print('Size = {}'.format(dl.get_size()))
print(dl)
print()

dl.add_to_head(25)
print('Size = {}'.format(dl.get_size()))
print(dl)
print()

dl.add_to_head(33)
print('Size = {}'.format(dl.get_size()))
print(dl)
print()

dl.add_to_head(1)
print('Size = {}'.format(dl.get_size()))
print(dl)
print()

dl.add(111, 1)
print('Size = {}'.format(dl.get_size()))
print(dl)
print()

dl.add_to_tail(150)
print('Size = {}'.format(dl.get_size()))
print(dl)
print()
