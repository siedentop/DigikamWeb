
# About
DigikamWeb is a web interface to Digikam (www.digikam.org). With it
you and others can browser your Digikam Database on the local network.

DigikamWeb is alpha software. Please let me know what you think: [Feedback](https://github.com/unapiedra/DigikamWeb/wiki/Feedback)

Bugs can be raised here:
  [Issue Tracker](https://github.com/unapiedra/DigikamWeb/issues)

# Getting started
*DigikamWeb is alpha software. Don't run it on your production database.*

## Requirements
You need Django and [sorl-thumbnail](http://sorl-thumbnail.readthedocs.org/en/latest/index.html). It is easiest to get them via [Pip](www.pip-installer.org).

    sudo pip install Django
    sudo pip install sorl-thumbnail

## Download
First, download DigkamWeb from [here](https://github.com/unapiedra/DigikamWeb/archive/master.zip).

Unpack it somewhere you like. In the following we will assume you copied it
to `/home/ada/DigikamWeb/`. 

For simplicity sake, we will also assume your Digikam Picture Collection is in
`/home/ada/Pictures/`.
## Database
Copy your Digikam Database into this folder. This way, we are never, ever touching the original database.  The Digikam database is called digikam4.db and you can find that file in the root
of your picture collection. Using the folders from above we get:

    cp /home/ada/Pictures/digikam4.db /home/ada/DigikamWeb/
## Settings
Open DigikamWeb/settings.py with a text editor of your choice. 
Change `MEDIA_ROOT`, `MEDIA_URL`, `PHOTO_URL` and `TEMPLATE_DIRS`. I moved those entries to the top of the `settings.py` file.

They should now become:

    MEDIA_ROOT = '/home/ada/DigikamWeb/tmp/'
    MEDIA_URL = '/home/ada/DigikamWeb/tmp/'
    PHOTO_URL = 'http://localhost:8080/'
    TEMPLATE_DIRS = ('/home/ada/DigikamWeb/digikam/templates')

## Starting Servers
We need to start three servers. It's not too bad though and maybe this will
change in the future. Okay then, here we go:

1. To server the static files call:
    cd /home/ada/DigikamWeb/static_files
    python -m SimpleHTTPServer 8081
2. To serve the photos (do this in a new terminal):
    cd /home/ada/Pictures
    python -m SimpleHTTPServer 8080
3. Start DigikamWeb (also in a new terminal):
    cd /home/ada/DigikamWeb/
    python manage.py syncdb # This will ask you to create an admin, please do.
    python manage.py runserver

## Using DigikamWeb
Use a webbrowser of your choice and go to: [http://localhost:8000/](http://localhost:8000/)
Because all the thumbnails have to be created first, the first load will take a
bit. But once the thumbnails are there, it is all very quick.

Click on an image to open that album.

## Stopping the servers
You can stop all servers by going into that terminal and pressing CTRL+C.

## Security
Please be aware that when you have DigikamWeb running, everybody can see these
pictures. Depending on your local setup, this might mean things are accessible
from the internet -- in most configurations though they are not.

# Features

* You can run DigikamWeb on your local laptop.
* You can have the images on a different server than the webserver for Digikam.
Just change `PHOTO_URL` in `settings.py`. And serve the images using Apache or `python -m SimpleHTTPServer port`

DigikamWeb doesn't change Digikam's database tables. Just read access
is necessary. It will also add its own tables. This doesn't effect Digikam.

# How it works
I created a Django app that connects to the Digikam database. The data is then
exposed with a RESTful API (`GET` only at the moment), which returns JSON files.

These JSON files are then loaded and displayed with JavaScript.

# How to help
## CSS
Please make the layout look pretty.
## JavaScript
* In the image view, I would like to make an image clickable and then get it
enlarged with the possibilities to navigate previous and next image.

## Django
Feel free to add Django Code. Please provide unit tests.

Unfortunately, to run tests, you have to change the MEDIA_ROOT and related fields in settings.py.
