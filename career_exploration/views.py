from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "career_exploration/index.html")
