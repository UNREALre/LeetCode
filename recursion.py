# -*- coding: utf-8 -*-
"""
Practicing with recursion
"""


def matreshka(n):
    if n > 1:
        print('Top side of matreshka #{}'.format(n))
        matreshka(n-1)
        print('Bottom side of matreshka #{}'.format(n))
    else:
        print('Final matreshka #{}'.format(n))

# matreshka(10)
# print()


def test_func(x):
    x += 5
    if x < 100:
        print('start = {}'.format(x))
        test_func(x)
        print('end = {}'.format(x))
    else:
        print("END")


test_func(50)


