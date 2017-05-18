# -*- coding: UTF-8 -*-
import sys
sys.path.append('/home/ndp/.ndt/platform/py')
#sys.path.append('/home/ndp/lihang/platform/searcher-4181_BRANCH/py')
#sys.path.append('/home/ndp/liuchang/lego/searcher-4181_BRANCH/py')
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
	retInfo['date'] = time.strftime('%Y-%m-%d',time.localtime(time.time())) 
	retInfo['msg']  = 'Hello World'

	return HttpResponse(json.dumps(retInfo))
