from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings

from django.views.static import serve

from django.conf.urls.static import static



urlpatterns = [
	path('admin/', admin.site.urls, name ='admin'),

	# Point to newsfeed.urls instead of having the url here (neater)
	# reference:  https://tutorial.djangogirls.org/en/django_urls/
	path('', include('newsfeed.urls')),
	path('', include('contact.urls')),
 

	# THIS IS IMPORTANT, REMEMBER THIS SHIT!!!!!!!! STATIC FILES, MEDIA FILES
	# THIS IS IMPORTANT, REMEMBER THIS SHIT!!!!!!!! STATIC FILES, MEDIA FILES
	re_path(r'^artworks_db/(?P<path>.*)$', serve, {'document_root' : settings.MEDIA_ROOT}),
	re_path(r'^static/(?P<path>.*)$', serve, {'document_root' : settings.STATIC_ROOT}),
	# THIS IS IMPORTANT, REMEMBER THIS SHIT!!!!!!!! STATIC FILES, MEDIA FILES
	# THIS IS IMPORTANT, REMEMBER THIS SHIT!!!!!!!! STATIC FILES, MEDIA FILES

] 
