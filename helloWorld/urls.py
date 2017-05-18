from django.conf.urls import url

from . import views

urlpatterns = [
	#url(r'[a-zA-Z0-9]{0,100}', views.upgrade, name='upgrade'),
	#url(r'^tasklist/$', views.upgrade, name='upgrade'),
	url(r'^$', views.index, name='index'),
]
