from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.views.generic.detail import DetailView


from .models import Post, SubForm, Projects
from .forms import ContactForm,SubscribeForm

# Create your views here.

class HomePageView(ListView):
	model = Post
	template_name ='index/home.html'
	ordering = ['-date']
	paginate_by = 3 #this shows 3 blog posts per page. No paginated object created??
	context_object_name = 'posts'



def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data.get('name')
			messages.success(request,f'Thank you {name}, your email has been sent. I will be in contact with you ASAP')
			return redirect(reverse('home'))

	else:
		form = ContactForm()
	return render(request,'index/contact.html', {'form': form})






def subscribe(request):
	'''
		function for the single model form that is rendered on the subscribe page
	'''



def about(request):
	return render(request, 'index/about.html',{})


class BlogPostDetailView(DetailView):
	model = Post
	template_name = 'index/detail.html'
	context_object_name = 'post'

def projects(request):
	context = Projects.objects.all()

	return render (request, 'index/projects.html',{'projects':context})