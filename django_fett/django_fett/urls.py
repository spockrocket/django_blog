from django.conf.urls import patterns, include, url
from django_fett.views import hello, hours, index

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index),
    # url(r'^blog/', include('blog.urls')),
	url(r'^hours/(\d{1,2})/$', hours),
    url(r'^admin/', include(admin.site.urls)),
    url('^hello/$', hello),
)
