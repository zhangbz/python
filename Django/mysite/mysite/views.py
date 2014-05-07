#!/usr/bin/env python
# coding=utf-8

#from django.template.loader import get_template
#from django.template import Context
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    current_date = datetime.datetime.now()
    #t = get_template('current_datetime.html')
    #html = t.render(Context({'current_date': now}))
    #return HttpResponse(html)
    return render_to_response('current_datetime.html', locals())

def hours_ahead(request, offset):
    try:
       hours_offset = int(offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours = hours_offset)
    assert True
    #html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    #return HttpResponse(html)
    return render_to_response('hours_ahead.html',locals())

def display_meta(request):
#做为一个练习，看你自己能不能把上面这个view函数改用Django模板系统来实现，而不是上面这样来手动输入HTML代码。 也可以试着把前面提到的 request.path 方法或 HttpRequest 对象的其它方法加进去。
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
