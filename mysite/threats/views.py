from django.http import HttpResponse
from django.conf import settings
from django.template import loader
import os

def data(request):
	file = open(os.path.join(settings.BASE_DIR, 'threats.json'))
	data = file.readlines()
	file.close()
	return HttpResponse(data, content_type='application/json')

def index(request):
	template = loader.get_template('threats/index.html')
	context = {}
	return HttpResponse(template.render(context, request))
