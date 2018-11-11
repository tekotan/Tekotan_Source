from django.shortcuts import render
from django.shortcuts import render
from .forms import *
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# Create your views here.
value = 'You have successfully signed up for email updates'
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')
        # check whether it's valid:
        if len(email) != 0 and len(name) != 0 and len(message) != 0:
            try:
                validate_email(email)
            except ValidationError as e:
                return render(request, 'about/index.html', {'result': 'Your email is not valid, please try again.'})
            else:
                send_mail('Message from: ' + name + "[" + email + "]" ,message ,'b.tanish@gmail.com', ['b.tanish@gmail.com',])
                return render(request, 'about/index.html', {'result': 'Your message has sent successfully.'})
        else:
            return render(request, 'about/index.html', {'result':''})




    # if a GET (or any other method) we'll create a blank form

    return render(request, 'about/index.html', {'result': ""})
