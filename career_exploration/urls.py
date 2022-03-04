from django.conf.urls import url

from . import views

app_name = "career_exploration"

urlpatterns = [url(r"^$", views.index, name="index")]
