from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=30)
	body = models.TextField()
	pubDate = models.DateTimeField()
	tags = TaggableManager()
	
	def __unicode__(self):
		return self.title
		
from django.contrib.syndication.views import Feed

class BlogFeed(Feed):
	title = "Blog"
	description = "Blog description"
	link = "/blog/feed/"
	
	def items(self):
		return Post.objects.all().order_by("-pubDate")[:5]
	def item_title(self, item):
		return item.title
	def item_description(self, item):
		return item.body
	def item_link(self, item):
		return u"/blog/%d" % item.id
