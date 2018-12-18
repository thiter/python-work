#!/usr/bin/env python
# coding=utf-8

def test_range():
    for i in range(8):
        print i


def n_test():
    test_list = [1, 3, 4, 'Hongten', 3, 6, 23, 'hello', 2]
    for i in range(len(test_list)):
        print i


def test_add(x):
    a = 10
    y = a + x
    print y


if __name__ == "__main__":
    # lst = fibs(5)
    # print lst
    n_test()
    # test_add(3)
    # test_range()
