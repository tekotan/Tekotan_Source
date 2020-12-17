from django.conf.urls import url

from . import views

app_name = "csa_projects"

urlpatterns = [url(r"^$", views.index, name="index")]
