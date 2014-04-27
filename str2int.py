#!/usr/bin/env python
# coding=utf-8

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    return reduce(fn, map(int, s))

#def str2int(s):
#    return reduce(lambda x,y: x*10+y, map(int, s))
