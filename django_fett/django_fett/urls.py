from django.conf.urls import patterns, include, url
# import any views you want...
from django_fett.views import index
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # regex to redirect urls to appropriate apps/pages
    url(r'^$', index),
    url(r'^contact/', include('contact.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    #~ url('^hello/$', hello),
    #~ url(r'^hours/(\d{1,2})/$', hours)
)
