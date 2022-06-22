from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

import datetime
import os
from django.conf import settings



# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length = 255)
	slug = models.SlugField(unique=True, max_length=255)
	content = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	author = models.TextField()

	def get_absolute_url(self):
		return reverse('blog_post_detail', args=[self.slug])

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)


	class Meta:
		ordering = ['created_on']

		def __unicode__(self):
			return self.title



class Comment(models.Model):
	name = models.CharField(max_length=42)
	email = models.EmailField(max_length=75)
	website = models.URLField(max_length=200, null=True, blank=True)
	content = models.TextField()
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	created_on = models.DateTimeField(auto_now_add=True)



class Artwork(models.Model):
	id = models.AutoField(null = False, primary_key=True)
	title = models.CharField(max_length=42, default = "No title yet.")
	category = models.CharField(max_length=42, default = "No category yet.")
	file = models.ImageField(upload_to='artworks/', height_field=None, width_field=None, max_length=100)
	full_file = models.ImageField(upload_to = 'artworks_full/', height_field = None, width_field = None, max_length=100, default=None)
	description = models.CharField(max_length=2000, default = "No description yet.")
	filter = models.CharField(max_length=42, default = "No filter yet.")
	date_post = models.DateField(default=datetime.date.today)


	class Meta:
		ordering = ['id']

		def __unicode__(self):
			return self.title
	



class CodeProject(models.Model):
	id = models.AutoField(null = False, primary_key=True)
	title = models.CharField(max_length=42, default = "No title yet.")
	category = models.CharField(max_length=42, default = "No category yet.")
	file = models.ImageField(upload_to='code_projects/', height_field=None, width_field=None, max_length=100)
	description = models.CharField(max_length=2000, default = "No description yet.")
	filter = models.CharField(max_length=42, default = "No filter yet.")
	date_post = models.DateField(default=datetime.date.today)

	class Meta:
		ordering = ['id']

		def __unicode__(self):
			return self.title

	def extension(self):
		file_extension = os.path.splitext(self.file.name)
		# return part 2 (aka index [1]) of the list called 'file_extension.'
		return file_extension[1]




class CodeDescriptionBlock(models.Model):
	id = models.AutoField(null = False, primary_key=True)
	file = models.ImageField(upload_to='code_description_blocks/', height_field=None, width_field=None, max_length=100)
	parent_id = models.IntegerField(default = 0, null = False)

	class Meta:
		ordering = ['parent_id']

		def __unicode__(self):
			return self.title
