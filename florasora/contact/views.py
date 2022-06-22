from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, Http404
from django.conf import settings
import environ

page_links = settings.GLOBAL_PAGE_LINKS
page_types = settings.GLOBAL_PAGE_TYPES

env = environ.Env()
environ.Env.read_env()

# Create your views here.
# https://stackoverflow.com/questions/11071983/django-form-is-valid-fails
# https://ordinarycoders.com/blog/article/build-a-django-contact-form-with-email-backend

# Django sending email with hotmail:
# https://www.serversettings.email/hotmail.com-email-server-settings-imap.php

def contact(request, *args, **kwargs):

    page_title_active = 'Contact'
    page_types_links = zip(page_types, page_links)
    host_email = env('EMAIL_HOST_USER')


    context = {
        'page_types_links' : page_types_links,
        'page_title_active' : page_title_active,
    }

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if (form.is_valid()):
            subject = "florasora.com - Message from " + form.cleaned_data['first_name']
            body = {
            'first_name': "First Name: " + form.cleaned_data['first_name'], 
            'last_name': "Last Name: " + form.cleaned_data['last_name'], 
            'email': "E-mail: " + form.cleaned_data['email_address'], 
            'message': "\nMessage:\n" + form.cleaned_data['message'], 
            }
            message = "\n".join(body.values())
            recipient = form.cleaned_data['email_address']
            try:
                send_mail(subject, message, host_email, [host_email], False) 
            except BadHeaderError:
                # context = context + {'error' : 'Invalid field data detected.'}
                context['error'] = 'Invalid field data detected'
                # return HttpResponse('Invalid header found.')
                return render(request, "contact.html", context)

            # context = context + {'message' : 'E-mail Sent!'}
            context['message'] = 'E-mail Sent! Thanks so much for taking the time!'
            return render(request, "contact.html", context)
        else:
            return HttpResponse('Request was not valid.')

    form = ContactForm()

    context = {
        'page_types_links' : page_types_links,
        'page_title_active' : page_title_active,
        'form':form,
    }


    return render(request, "contact.html", context)