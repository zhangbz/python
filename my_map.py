#!/usr/bin/env python
# coding=utf-8

#my_map

def my_map(f, *list):
    newlist = []
    for x in list:
        newlist.append(f(x))
    return newlist

def my_func(x):
    if isinstance(x, (int, float)):
        return x * x
    else:
        return "is not number"

print my_map(my_func, *(1, 2, "abc", 4))
