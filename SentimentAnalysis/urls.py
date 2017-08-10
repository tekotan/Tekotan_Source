from django.conf.urls import url

from . import views
app_name = 'SentimentAnalysis'

urlpatterns = [
	url(r'^$', views.evaluate, name='evaluate'),
]
