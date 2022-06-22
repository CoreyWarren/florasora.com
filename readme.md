# florasora.com - Website Django Project README

```bash
# To refresh the server after changing most files (HTML, CSS, JS)

sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo nginx -t && sudo systemctl restart nginx
```


#

# Running the server on winenv Environment (Windows 10):

```python
# settings.py - Use these settings:

DEBUG = True
ALLOWED_HOSTS = []

STATICFILES_DIRS = (
   os.path.join(BASE_DIR, 'static'),
)
```

```bash
# To run the (winenv) on Windows Environment for Django:

& winenv/Scripts/Activate.ps1
```
> Yes, the "&" is necessary. 


```bash
# While in (winenv), run:

python manage.py runserver --insecure
```

> Interestingly enough, because your windows environment and linux environment are separate (for python/django), your super-user in your linux environment is NOT the same as your super-user in your windows environment. This also means you will need to create superusers separately in both your winenv and linux env:

```bash
# Create a super user for BOTH python environments (1 - Linux, 2 - Windows):

python manage.py createsuperuser --username=cocothegorilla
```



# Initial Setup for mySQL, Django, Ubuntu, etc...:

## Setting up Django with Nginx, Postgres, and Gunicorn (on DigitalOcean):
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04

> Tips:
>
> When you try to run gunicorn after adding the gunicorn.service file, but something goes wrong, it's probably because the directories you listed are wrong. Check all ...3? places where you list your own directory in the 'gunicorn.service' file. It is a very likely source of your problems. Also, don't forget to check for random added or deleted characters in the service file.
>
>> Protip : When fixing the gunicorn.service file, don't forget to run:
>> ```
>> sudo systemctl daemon-reload
>> sudo systemctl restart gunicorn
>> ```
>> And when you run:
>> ```
>> sudo journalctl -u gunicorn
>> ```
>> Don't forget to SCROLL to the bottom of the output, where all the latest output is. Otherwise, you are only READING OLD ERRORS. Don't waste time with that.


## Get your custom domain to connect to your website:
https://www.digitalocean.com/community/questions/how-to-set-domain-name-django-nginx-ubuntu-16-04



## Fixing Nginx Welcome Page:
https://www.youtube.com/watch?v=MP3Wm9dtHSQ


## Handling "www.(...)" Redirects:
https://www.youtube.com/watch?v=6QYJUvrb7m8

## lookup domain names on ICANN Lookup Tool:
https://lookup.icann.org/en

## certbot for nginx servers on ubuntu machines:
https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal
https://letsencrypt.org/documents/LE-SA-v1.2-November-15-2017.pdf





# Adding images to the site
### Even though they're [background images] and {% static %} is being super weird (and is throwing errors):

https://simpleit.rocks/python/django/call-static-templatetag-for-background-image-in-css/

> Lesson learned: it's okay to throw errors.

# Connecting to the mySQL database remotely and syncing it between two devices

This is the filepath for the mysql settings.
```
/etc/mysql/mysql.conf.d/mysqld.cnf
```

https://stackoverflow.com/questions/4093603/how-do-i-find-out-my-mysql-url-host-port-and-username

TCP Forwarding on host (remote) server for TCP/IP connection:
https://serverfault.com/questions/616696/lost-connection-to-mysql-server-at-reading-initial-communication-packet-syste

Digital Ocean specific:
https://www.digitalocean.com/community/questions/how-do-i-use-ssh-to-access-mysql-remotely


## We need to take some steps to shut down mySQL so that we can edit the root password and access the default database.


```bash
# All-in One Package:
# includes Apache, phpMyAdmin, mySQL, etc...

https://www.apachefriends.org/index.html
```



https://www.inmotionhosting.com/support/edu/cpanel/kill-mysql-processes-phpmyadmin/

https://www.wikihow.com/Install-phpMyAdmin-on-Your-Windows-PC

## Actual easy apache download windows 10:

https://www.apachelounge.com/download/
https://www.youtube.com/watch?v=oJnCEqeAsUk
> PROTIP: Watch the installation directory and unzip process carefully. You unzip into your drive directory, not just anywhere!

install php (on windows 10, 2021)
https://www.youtube.com/watch?v=QMWb_Wn2g5k


## How To Secure MySQL Replication Using SSH on a VPS:

https://www.digitalocean.com/community/tutorials/how-to-secure-mysql-replication-using-ssh-on-a-vps

## How to copy files via SSH :
https://unix.stackexchange.com/questions/106480/how-to-copy-files-from-one-machine-to-another-using-ssh


## pymysql, mysqlclient, etc for Python mysql integration (help):

https://www.a2hosting.com/kb/developer-corner/mysql/connecting-to-mysql-using-python

## Strict mode in phpMyAdmin for mySQL:

https://stackoverflow.com/questions/37964325/how-to-find-and-disable-mysql-strict-mode

## Adding objects to django database in django shell (models):

https://docs.djangoproject.com/en/4.0/intro/tutorial02/

## Django admin area not showing models / database objects:

https://stackoverflow.com/questions/24813536/django-admin-not-showing-models/24814041

> "Double-check that you've actually registered your models in admin.py"

```py
from MyApp.models import MyModel
admin.site.register(MyModel)
```

> Protip: it may need to be in the APP folder, not your PROJECT folder. I.E.:
> > "project/blog/admin.py" rather than "project/admin.py"

## Display image files from a django model 

https://stackoverflow.com/questions/9498012/how-to-display-images-from-model-in-django/9498359


## Best practices when working with Django models:

https://steelkiwi.com/blog/best-practices-working-django-models-python/

## Displaying one django database object at a time:

https://stackoverflow.com/questions/31942843/displaying-one-django-database-object-on-a-page-at-a-time

## nginx setup with media and static folders for django (serving media files on deployed live website with debug = false):

https://stackoverflow.com/questions/20392741/nginx-errorlocation-directive-is-not-allowed-here-in-etc-nginx-nginx-conf76

## upload_to error

```
newsfeed.Artwork.file: (fields.E202) ImageField's 'upload_to' argument must be a relative path, not an absolute path.
        HINT: Remove the leading slash.
```

```bash
# try 
upload_to = 'artworks/'
# because settings.MEDIA_ROOT is absolute. We want relative!
```

## Variables in Django Templates Help:

> Declaring variables:
>
> https://stackoverflow.com/questions/34710043/how-to-declare-variables-inside-django-templates/34710719

> Access Array Indices:
>
> https://stackoverflow.com/questions/28872390/django-how-to-access-array-index-in-template-using-variable

> Error Handling Try/Except in Django:
>
> https://stackoverflow.com/questions/8524077/catching-exceptions-in-django-templates

> "'xyz' tag is not a registered tag library":
> 
> https://stackoverflow.com/questions/40686201/django-1-10-1-my-templatetag-is-not-a-registered-tag-library-must-be-one-of

> > "How about we skip all that and just use ZIP two combine the two dictionaries?"
> >
> > https://groups.google.com/g/django-users/c/rucw6bKFdz8?pli=1
> >
> > https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/
> > 
> > https://www.adamsmith.haus/python/answers/how-to-zip-two-lists-in-python


## Customizing django's pre-made templates:

https://docs.djangoproject.com/en/dev/topics/forms/#customizing-the-form-template

## Django email settings:

https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-EMAIL_TIMEOUT

## gitignore documentation:

https://git-scm.com/docs/gitignore

## Displaying alert messages with Django:

https://www.youtube.com/watch?v=AkkBc_d7OXk

## Appending to python dictionaries (for context return, for example):

https://www.guru99.com/python-dictionary-append.html

## Python if, elif, endif, etc in Django:

https://stackoverflow.com/questions/39247352/how-to-check-if-elif-else-conditions-at-the-same-time-in-django-template

## How to TEST (unit tests) django URLs:

https://stackoverflow.com/questions/18987051/how-do-i-unit-test-django-urls
