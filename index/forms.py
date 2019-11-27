from django import forms
from django.forms import ModelForm

from . models import SubForm
from . validators import validate_domain_email



class ContactForm(forms.Form):
	name = forms.CharField( max_length = 100, required= True)
	from_email = forms.EmailField(required=True,label = 'Enter your email',
								 validators=[validate_domain_email])
	
	subject = forms.CharField(required=True)
	message = forms.CharField(widget=forms.Textarea,required=True)


class SubscribeForm(ModelForm):
	class Meta:
		model = SubForm
		fields = ['name','email']


	def __str__(self):
		return self.Email
