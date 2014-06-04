from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post, BlogFeed

urlpatterns = patterns('blog.views',
    url(r'^$', 'blogview'),
	url(r'^(?P<pk>\d+)$', DetailView.as_view(
		model=Post,
		template_name="post.html")
		),
	url(r'^archives/$', ListView.as_view(
		queryset=Post.objects.all().order_by("-pubDate"),
		template_name="archives.html")
		),
	url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
	url('^feed/$', BlogFeed()),
	
)

