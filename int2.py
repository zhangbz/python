#!/usr/bin/env python
# coding=utf-8

import functools
int2 = functools.partial(int, base=2)

#def int2(x, base=2):
#    return int(x,base)
