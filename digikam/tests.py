# Copyright 2013 Christoph Siedentop <digikamweb@siedentop.name>
"""

"""

from django.test import TestCase
from digikam.models import Image, Album, AlbumRoot, Tag, ImageTag
import settings
import json

class ThumbailTest(TestCase):
  def setUp(self):
    ar = AlbumRoot()
    ar.save()
    album = Album(albumroot=ar, relativepath='')
    album.save()
    self.assertEqual(1, album.id)
    image1 = Image(id=0, name='foo0.jpg', status=3, category=1, album=album)
    image1.save()
    image2 = Image(id=1, name='foo1.jpg', status=3, category=1, album=album)
    image2.save()
    image3 = Image(id=2, name='foo2.jpg', status=3, category=1, album=album)
    image3.save()
    # Some tags
    tag = Tag(name='aTag')
    tag.save()
    it = ImageTag(image=image1, tag=tag)
    it.save()
    it = ImageTag(image=image2, tag=tag)
    it.save()
  def test_getThumbnail(self):
    ''' Test that a thumbnail is created.
    '''
    resp = self.client.get('/thumbnail/0/100')
    self.assertEqual(resp.status_code, 200)
    self.assertTrue('url' in resp.content)
  def test_thumbnailSize(self):
    ''' Two thumbnails of the same image with different sizes must not have
    the same url.
    '''
    resp = self.client.get('/thumbnail/0/100')
    self.assertEqual(resp.status_code, 200)
    self.assertTrue('url' in resp.content)
    result = json.loads(resp.content)
    resp2 = self.client.get('/thumbnail/0/400')
    result2 = json.loads(resp2.content)
    self.assertNotEqual(result['url'], result2['url'])
    
  def test_getSelection(self):
    ''' Test that we get a list of images for given album
    '''
    expected = '{"images": [0, 1, 2]}'
    resp = self.client.get('/album/1.json')
    self.assertEqual(resp.status_code, 200)
    self.assertEqual(expected, resp.content)
  def test_getSelectionEmpty(self):
    resp = self.client.get('/album/2.json')
    expected = '{"error": "Album does not exist."}'
    self.assertEqual(expected, resp.content)

  #def test_getTagByName(self):
    #'''
    #Test that we get image 1 and 2 associated with tag 'aTag'
    #'''
    #expected = json.dumps({'images': [0, 1]})
    #resp = self.client.get('/tag/aTag.json')
    #self.assertEqual(expected, resp.content)
  #def test_getTagByNameSpaces(self):
    #resp = self.client.get('tag/a Tag.json')

  def test_getTagById(self):
    expected = json.dumps({'images': [0, 1]})
    resp = self.client.get('/tag/1.json')
    self.assertEqual(expected, resp.content)

  def test_getLatestAlbums(self):
    expected = json.dumps({'albums': [{'id':1, 'coverId':0}]})
    response = self.client.get('/latestAlbums.json')
    self.assertEqual(expected, response.content)
