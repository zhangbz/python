#!/usr/bin/env python
# coding=utf-8

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s call %s()' % (text, func.__name__)
            print func(*args, **kw)
            print 'end call'
        return wrapper
    return decorator

@log('zhangbz')
def now():
    print '2014-04-27'

