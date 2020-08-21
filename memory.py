# -*- coding: utf-8 -*-
"""Practicing with memory management"""

x = 5
print('id(x) = {}'.format(id(x)))
y = x
print('y = {}, id(y) = {}'.format(y, id(y)))
x = 10
print('id(x) = {}'.format(id(x)))
print('y = {}, id(y) = {}'.format(y, id(y)))

str1 = "abc"
print('str1 = {}, id(str1) = {}'.format(str1, id(str1)))
str2 = str1
print('str2 = {}, id(str2) = {}'.format(str2, id(str2)))
str1 = "def"
print('str1 = {}, id(str1) = {}'.format(str1, id(str1)))
print('str2 = {}, id(str2) = {}'.format(str2, id(str2)))

str3 = "python is cool!"
str4 = "python is cool!"
print('str3 is str4: {}'.format(str3 is str4))
print('id(str3) = {}; id(str4) = {}'.format(id(str3), id(str4)))


class test2:
    def __init__(self, val):
        self.data = val


class test:
    def __init__(self, val):
        self.data = val

    def set_new_val(self, val):
        print('self.data = {}, id(self.data) = {}'.format(self.data, id(self.data)))
        new_obj = test2(self.data)
        print('new_obj.data = {}, id(new_obj.data) = {}'.format(new_obj.data, id(new_obj.data)))
        self.data = val
        print('self.data = {}, id(self.data) = {}'.format(self.data, id(self.data)))
        print('new_obj.data = {}, id(new_obj.data) = {}'.format(new_obj.data, id(new_obj.data)))

test = test(25)
test.set_new_val(33)


def my_func(x):
    x = 5


x = 10
my_func(x)
print('x = {}'.format(x))
