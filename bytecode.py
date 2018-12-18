#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "thiter"


def testcode():
    a = 'hello,中国'
    b = u'Hello,中国'

    print type(a), len(a), a
    print type(b), len(b), b


def testcode1():
    str1 = u"你好"
    print type(str1), str1

    str2 = str1.encode("utf-8")
    print type(str2), str2


if __name__ == '__main__':
    testcode1()
    print "------"
    testcode1()
