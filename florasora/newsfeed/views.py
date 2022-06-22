from django.http import HttpResponse
from django.shortcuts import render
from .models import Artwork, CodeProject
from django.http import Http404
from django.conf import settings


page_links = settings.GLOBAL_PAGE_LINKS
page_types = settings.GLOBAL_PAGE_TYPES





#
# HOMEPAGE:
#
def index(request, *args, **kwargs):

    page_title_active = "Portfolio"
    page_types_links = zip(page_types, page_links)

    # Sanity Check code:
    print("args, kwargs: ", args, ", ", kwargs)
    print("Site User: ", request.user)

    try:
        artworks = Artwork.objects.all()
    except:
        raise Http404("Could not retrieve all artworks from database.")

    try:
        code_projects = CodeProject.objects.all()
    except:
        raise Http404("Could not retrieve all code projects from database.")

    # return basic index render (homepage for florasora.com!)
    # all_works will be used to refer to our list of all artworks in the HTML code for this 'index' render.
    return render(request, "portfolio.html", {
        'page_types_links' : page_types_links,
        'page_title_active' : page_title_active,
        'artworks' : artworks,
        'code_projects' : code_projects,
        })
    # {} here is an empty dictionary, will be used later.




#
# SINGLE ART VIEW:
#
def art_view(request, this_artwork_id):

    page_title_active = 'none'
    page_types_links = zip(page_types, page_links)
    

    # "Retrieve" this specific object using filters
    # Help : https://docs.djangoproject.com/en/2.2/topics/db/queries/ # - For queries
    # Help : https://docs.djangoproject.com/en/4.0/intro/tutorial03/ # - For views.py and urls.py
    try:
        # retrieve the database object for use in-page
        this_artwork = Artwork.objects.get(id = this_artwork_id)
        artwork_database_length = Artwork.objects.count()
    except:
        raise Http404("Corey - Artwork does not exist at %d", this_artwork_id)


    # Previous Artwork ID (for 'prev' button on page):
    prev_artwork_calc = (this_artwork_id - 1) % artwork_database_length
    if(prev_artwork_calc < 1):
        prev_artwork = artwork_database_length
    else:
        prev_artwork = prev_artwork_calc


    # Next Artwork ID (for 'next' button on page):
    next_artwork_calc = (this_artwork_id + 1) % artwork_database_length
    if(next_artwork_calc == 0):
        next_artwork = artwork_database_length
    else:
        next_artwork = next_artwork_calc


    # return this object in the render, using the URL defined in urls.py in this folder.
    return render(request, "portfolio-single.html", {
        'page_types_links' : page_types_links,
        'page_title_active' : page_title_active,
        'this_artwork' : this_artwork ,
        'artwork_database_length' : artwork_database_length,
        'prev_artwork' : prev_artwork,
        'next_artwork' : next_artwork
            }
        )




#
# SINGLE CODE VIEW:
#
def code_view(request, this_code_project_id):

    page_title_active = 'none'
    page_types_links = zip(page_types, page_links)

    # "Retrieve" this specific object using filters
    # Help : https://docs.djangoproject.com/en/2.2/topics/db/queries/ # - For queries
    # Help : https://docs.djangoproject.com/en/4.0/intro/tutorial03/ # - For views.py and urls.py
    try:
        # retrieve the database object for use in-page
        this_code_project = CodeProject.objects.get(id = this_code_project_id)
        code_project_database_length = CodeProject.objects.count()
    except:
        raise Http404("Corey - Code Project does not exist at %d", this_code_project_id)


    # Previous code_project ID (for 'prev' button on page):
    prev_code_project_calc = (this_code_project_id - 1) % code_project_database_length
    if(prev_code_project_calc < 1):
        prev_code_project = code_project_database_length
    else:
        prev_code_project = prev_code_project_calc


    # Next code_project ID (for 'next' button on page):
    next_code_project_calc = (this_code_project_id + 1) % code_project_database_length
    if(next_code_project_calc == 0):
        next_code_project = code_project_database_length
    else:
        next_code_project = next_code_project_calc

    # return this object in the render, using the URL defined in urls.py in this folder.
    return render(request, "portfolio-single-code.html", {
        'page_types_links' : page_types_links,
        'page_title_active' : page_title_active,
        'this_code_project' : this_code_project ,
        'code_project_database_length' : code_project_database_length,
        'prev_code_project' : prev_code_project,
        'next_code_project' : next_code_project
            }
        )



#
# 'ABOUT ME' PAGE:
#
def about_me(request, *args, **kwargs):

    page_title_active = 'About Me'
    page_types_links = zip(page_types, page_links)

    context = {
        'page_types_links' : page_types_links,
        'page_title_active' : page_title_active,
    }
    return render(request, "about_me.html", context)


#
# 'COMING SOON' PAGE:
#
def coming_soon(request, *args, **kwargs):
    
    page_title_active = 'none'
    page_types_links = zip(page_types, page_links)

    return render(request, "coming_soon.html", {
        'page_types_links' : page_types_links,
        'page_title_active' : page_title_active,
    })



