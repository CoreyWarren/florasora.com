from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [


    # HOMEPAGE:
    path('', views.index, name='index'),


    # SINGLE ARTWORK VIEW:
    # follow this guide closely to understand urls.py <-> views.py:
    # https://docs.djangoproject.com/en/4.0/intro/tutorial03/
    path('<int:this_artwork_id>/single-artwork/', views.art_view, name='art_view'),


    # SINGLE CODE PROJECT VIEW:
    path('<int:this_code_project_id>/single-code-project/', views.code_view, name='code_view'),
    

    # SUBSTITUTE FOR UPCOMING PAGES:
    path('coming_soon/', views.coming_soon, name='coming_soon'),

    path('about_me/', views.about_me, name='about_me'),

]


if(settings.DEBUG == True):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Helping with retrieving images from MEDIA_ROOT
# (Specifically added to help with DEBUG=TRUE errors with displaying images from the database,
# which also has its images stored in the django project in a folder I can see in the 
# file explorer):


