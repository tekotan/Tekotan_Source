from django.conf.urls import url

from . import views
app_name = 'mult'

urlpatterns = [
	url(r'^$', views.get_ingredients, name='get_ingredients'),
]