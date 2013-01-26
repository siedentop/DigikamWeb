# Copyright 2013 Christoph Siedentop <digikamweb@siedentop.name>
from digikam.models import Album, Image, Tag
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
import json
from sorl.thumbnail import get_thumbnail

def index(request):
    latest_album_list = Album.objects.all().order_by('-date')[:20]
    return render_to_response('index.html', {'latest_album_list': latest_album_list})

def getThumbnail(request, image_id, size):
    ''' Returns JSON of Thumbnail URL '''
    try:
      image = Image.objects.get(pk=image_id)
    except ObjectDoesNotExist:
      return HttpResponse(json.dumps({'error':'Image does not exist.'}), mimetype='application/json')
    req = {}
    thumb = get_thumbnail(image.getUrl(), size, crop='center')
    req['url'] = thumb.url
    response = json.dumps(req)
    return HttpResponse(response, mimetype='application/json')

def albumJson(request, album_id):
  ''' Returns Images related to Album in JSON.'''
  try:
    album = Album.objects.get(pk=album_id)
    images = Image.objects.filter(album=album)
    req = {}
    imageIdList = [im.id for im in images]
    req['images'] = imageIdList
  except ObjectDoesNotExist:
    req = {'error':'Album does not exist.'}
  response = json.dumps(req)
  return HttpResponse(response, mimetype='application/json')

def tagJson(request, tag_id):
  ''' Returns JSON with images associated with given tag_id.'''
  try:
    tag = Tag.objects.get(id = tag_id)
  except ObjectDoesNotExist:
    req = {'error':'Tag %s does not exist.' % tag_id}
    return HttpResponse(json.dumps(req), mimetype='application/json')
  images = tag.images.all()
  imageIdList = [im.id for im in images]
  req = {'images': imageIdList}
  return HttpResponse(json.dumps(req), mimetype='application/json')

def latestAlbumsJson(request):
  ''' Returns JSON formated list of latest albums.
  
  id is the Album ID
  coverId is the Image ID for the cover of the album.
  '''
  latest_album_list = Album.objects.all().order_by('-date')[:20]
  ids = [{'id':album.id, 'coverId':album.getCover()} for album in latest_album_list]
  return HttpResponse(json.dumps({'albums': ids}), mimetype='application/json')
