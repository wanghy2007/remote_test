from django.http import HttpResponse
from django.conf import settings
import os

def index(request):
	file = open(os.path.join(settings.BASE_DIR, 'threats.json'))
	data = file.readlines()
	file.close()
	return HttpResponse(data, content_type='application/json')
