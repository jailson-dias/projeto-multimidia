from django.conf.urls import url, include

from core import views

app_name = 'core'
urlpatterns = [
	url(r'^$', views.home, name='index'),
	url(r'^(?P<pk>[0-9]+)/', views.exibir, name='exibir'),
]