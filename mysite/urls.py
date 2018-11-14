"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin
from mysite.settings import STATIC_ROOT
from django.views.static import serve
from django.http import HttpResponseRedirect

urlpatterns = [
    url(r"^$", include("tekotan.urls")),
    url(r"^Sentiment_Analysis/", include("SentimentAnalysis.urls")),
    #    url(r'^recipe_extraction/', include('recipe_extraction.urls')),
    #    url(r'^calculator/', include('calculator.urls')),
    url(r"^signup/", include("signup.urls")),
    url(r"^csp/", include("csp_projects.urls")),
    url(r"^other/", include("other_projects.urls")),
    url(r"^experience/", include("work_experience.urls")),
    url(r"^tensorflow/", include("tensorflow_projects.urls")),
    url(r"^admin/", admin.site.urls),
    url(r"^static/(.*)$", serve, {"document_root": STATIC_ROOT, "show_indexes": True}),
    url(r"^about_me/", include("about_me.urls")),
]
