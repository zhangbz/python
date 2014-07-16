#!/usr/bin/env python
# coding=utf-8

def application(environ, start_response):
    start_response('200 0k', [('Content-Type', 'text/html')])
    return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
