from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Post
from .models import SubForm


def validate_domain_email(value):
	if not '@gmail.com' in value:
		raise ValidationError(_('sorry, please enter a valid gmail account'))
	return value

#put in a validator that checks to see if the email is already in the database

def validate_email_already_in_database(value):
	if not value in SubForm.objects.filter(email = value):
		return value

	else:
		raise ValidationError(_(' looks like this email was already on our subscription list'))