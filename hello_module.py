#!/usr/bin/env python
# coding=utf-8

'a test module'    #任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'zhangbz'

#以上为python模块的的标准文件模板

import sys 

def test():
    args = sys.argv
    if len(args) == 1:
        print 'Hello, world!'
    elif len(args) == 2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__ == '__main__':
    test()
