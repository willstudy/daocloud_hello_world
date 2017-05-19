# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template import Context 

import time
import json

# Create your views here.

def index(request):
	retInfo = {}
	retInfo['date'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) 
	retInfo['msg']  = 'Hello World'

	context = RequestContext(request, {
		'ret_info': json.dumps(retInfo)
	})

	#return render(request, 'index.html', context)
	return HttpResponse(json.dumps(retInfo))
