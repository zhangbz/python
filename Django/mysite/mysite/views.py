#!/usr/bin/env python
# coding=utf-8

from django.template import Template, Context
from django.http import Http404, HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    #Simple way of using templates from the filesystem.
    #This is BAD because it doesn't account for missing  files!
    fp = open('/root/python/Django/mysite/mysite/templates/mytemplate.html')
    t = Template(fp.read())
    fp.close()
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
       offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    assert True
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
