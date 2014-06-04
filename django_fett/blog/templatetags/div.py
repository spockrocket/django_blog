from django import template
 
register = template.Library()


def count_div(value, arg):
	try:
		return int(int(value)/int(arg))
	except template.ValueError:
		return "Oops"
register.filter('div', count_div)
