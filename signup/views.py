from django.shortcuts import render
from .forms import *
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Person
# Create your views here.
value = 'You have successfully signed up for email updates'
def evaluate(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        email = request.POST.get('email')
        firstname = request.POST.get('First_name')
        lastname = request.POST.get('Last_name')
        # check whether it's valid:
        if len(email) != 0 and len(firstname) != 0 and len(lastname) != 0:
            try:
                validate_email(email)
            except ValidationError as e:
                return render(request, 'signup/index.html', {'result': 'the email is not valid, please try again'})
            else:
                msg = 'Hi ' +firstname+" "+lastname+ ", thank you for signing up for the tekotan mailing list. This ensures that you don't miss out on any of my new posts"
                send_mail('Confirmation for Tekotan Emailing list',msg,'b.tanish@gmail.com', [email,])
                p = Person.objects.create(first_name=firstname, last_name=lastname, email=email)
                return render(request, 'signup/index.html', {'result': 'You have successfully signed up for email updates'})
        else:
            return render(request, 'signup/index.html', {'result':''})




    # if a GET (or any other method) we'll create a blank form

    return render(request, 'signup/index.html', {'result': ""})
