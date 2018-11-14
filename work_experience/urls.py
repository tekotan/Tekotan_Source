from django.conf.urls import url

from . import views

app_name = "work_experience"

urlpatterns = [url(r"^$", views.index, name="index")]
