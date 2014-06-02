from django.conf.urls import patterns, include, url
    
urlpatterns = patterns('contact.views',
    # regex to redirect urls to appropriate apps/pages
    (r'^$', 'contactview'),
	(r'^thanks/', 'thanks'),

)
