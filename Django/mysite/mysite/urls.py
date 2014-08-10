from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, hours_ahead, display_meta
from django.contrib import admin
from mysite.books import views
from mysite.contact import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^hello/$', hello),
    url('^time/$', current_datetime),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^display_meta/$', display_meta),
    #url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
)
