from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.mail import send_mail, BadHeaderError
from contact.models import ContactMe

def thanks(request):
	title = 'Thanks for the input!'
	section = 'thanks'
	return render_to_response('thanks.html', {'title': title, 'section': section})

def contactview(request):
	title = 'Contact Me'
	section = 'contact'
	if request.method == 'POST':
		form = ContactMe(request.POST) # A form bound to the POST data
		if form.is_valid():
			name = form.cleaned_data['name']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			send_to_myself = form.cleaned_data['send_to_myself']
			recipients = ['admin@spockrocket.com']
			if send_to_myself:
				recipients.append(sender)		
		send_email(name, subject, message, sender, recipients)
	else:
		form = ContactMe() # An unbound form
	return render(request, 'contact.html', {'form': form,'title': title, 'section': section})

def send_email(name, subject, message, sender, recipients):
	if not name:
		name = 'Anonymous'
	if subject and message and sender and recipients:
		try:
			msg = "%s says:\n %s" % (name, message)
			send_mail(subject, msg, sender, recipients)
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
		return HttpResponseRedirect('/contact/thanks/')
	else:
		return HttpResponse('Make sure all fields are entered and valid.')
