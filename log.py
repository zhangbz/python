#!/usr/bin/env python
# coding=utf-8

import functools

def log(text):
    if not isinstance(text, str):
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print 'call function %s()' % text.__name__
            print text(*args, **kw)
            print 'end call'
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print '%s call function %s()' % (text, func.__name__)
                print func(*args, **kw)
                print 'end call'
            return wrapper
        return decorator

@log('zhangbz')
def now():
    print '2014-04-27'

now()
