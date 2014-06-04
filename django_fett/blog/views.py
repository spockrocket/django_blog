from django.shortcuts import render_to_response
from blog.models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
def blogview(request):
	title = "My Projects Blog"
	section = 'blog'
	queryset=Post.objects.all().order_by("-pubDate")[:3]
	return render_to_response('blog.html', {'post_list': queryset[1:], 'last': queryset[0], 'title': title, 'section': section})

def tagpage(request, tag):
	title = "Posts tagged "
	section = 'tagpage'
	posts = Post.objects.filter(tags__name=tag)
	return render_to_response("tagpage.html",{"posts":posts, "tag":tag, 'title': title, 'section': section})
