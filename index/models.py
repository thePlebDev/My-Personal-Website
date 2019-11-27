from django.db import models





# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	about = models.CharField(max_length=200)
	date = models.DateField()
	last_edited = models.DateField(auto_now=True)
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	content= models.TextField()
	urls = models.URLField( )

	class Meta:
		verbose_name_plural = 'Posts'

	def __str__(self):
		return self.title


class SubForm(models.Model):
	name = models.CharField(max_length = 200)
	email = models.EmailField(max_length=200)

	verbose_name_plural =  'Emails From User'

	def __str__(self):
		return  f'{self.name}s email'



class Projects(models.Model):
	title = models.CharField(max_length=200)
	about = models.TextField()
	date = models.DateField()
	github_url = models.URLField(max_length=200)
	live_project_url = models.URLField(max_length=200)

	def __str__(self):
		return self.title
	






