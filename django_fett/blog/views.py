from django.shortcuts import render_to_response
from blog.models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
def blogview(request):
	title = "My Projects Blog"
	section = 'blog'
	desc = 'This is my blog'
	lede = 'Here, you can follow my various projects and thoughts.'
	queryset=Post.objects.all().order_by("-pubDate")[:3]
	return render_to_response('blog.html', {'post_list': queryset[1:], 'last': queryset[0], 'title': title, 'section': section, 'page_desc': desc, 'lede': lede})

def tagpage(request, tag):
	title = "Tagged Posts"
	section = 'tagpage'
	desc = 'Posts tagged: \"%s\"' % tag
	posts = Post.objects.filter(tags__name=tag)
	return render_to_response("tagpage.html",{"posts":posts, "tag":tag, 'title': title, 'section': section, 'page_desc': desc})

def postview(request):
	title = ''
