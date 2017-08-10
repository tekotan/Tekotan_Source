from django import forms

class get_email(forms.Form):
	email = forms.CharField(label='email', max_length=100)
class get_first_name(forms.Form):
    first_name = forms.CharField(label='First_name')
class get_last_name(forms.Form):
    lastname = forms.CharField(label='Last_name')
