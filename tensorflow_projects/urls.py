from django.conf.urls import url

from . import views

app_name = "tensorflow_projects"

urlpatterns = [url(r"^$", views.index, name="index")]
