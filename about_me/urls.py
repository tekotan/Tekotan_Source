from django.conf.urls import url

from . import views

app_name = "about_me"

urlpatterns = [url(r"^$", views.index, name="index")]
