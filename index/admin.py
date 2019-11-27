from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

from .models import Post, SubForm,Projects

# Register your models here.

class TutAdmin(admin.ModelAdmin):
	formfield_overrides ={
		models.TextField: { 'widget': TinyMCE()}
	}




admin.site.register(Post,TutAdmin)

admin.site.register(SubForm)

admin.site.register(Projects,TutAdmin)
