from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, hours_ahead
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^hello/$', hello),
    url('^time/$', current_datetime),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
)
