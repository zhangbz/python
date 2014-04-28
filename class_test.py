#!/usr/bin/env python
# coding=utf-8

def Std(object):
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print '%s' % self.name

zhangbz = Std('zhangbz')
#zhangbz.age = 1
zhangbz.print_name()
