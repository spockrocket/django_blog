from django.http import Http404, HttpResponse
from django.template import Context, Template
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime

def hello(request):
	return HttpResponse("Hello there, this is new!")

def index(request):
	return render_to_response('base.html',)



def hours(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	now = datetime.datetime.now() + datetime.timedelta(hours=offset)
	tpl = get_template('hours.html')
	html = tpl.render(Context({'offset': offset, 'date': now}))
	# same thing, short hand
	# return render_to_response('hours.html', {'offset': offset, 'date': now})
	return HttpResponse(html)

