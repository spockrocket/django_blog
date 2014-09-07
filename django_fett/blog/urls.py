from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post, BlogFeed

urlpatterns = patterns('blog.views',

    url(r'^$', 'blogview'),
    
    # old DetailView code of individual posts
	#~ url(r'^(?P<pk>\d+)$', DetailView.as_view(
		#~ model = Post,
		#~ template_name = "post.html")
		#~ ),

	url(r'^(?P<pk>\d+)$', 'postview'),
		
	url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
	
	url(r'^archives/$', 'archives'),
	
	url('^feed/$', BlogFeed()),
)

