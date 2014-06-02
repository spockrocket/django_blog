from django.conf.urls import patterns, include, url
# import any views you want...
from django_fett.views import hello, hours, index
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # regex to redirect urls to appropriate apps/pages
    url(r'^$', index),
	url(r'^hours/(\d{1,2})/$', hours),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url('^hello/$', hello),
)
