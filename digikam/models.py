# Copyright 2013 Christoph Siedentop <digikamweb@siedentop.name>

from django.db import models
import settings
import os

def sanitise(url):
    new = url.replace(' ', '%20')
    return new
    if (url.count(' ') > 0):
        return ''
    return url

class AlbumRoot(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(blank=True, max_length=200)
    status = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    identifier = models.TextField(blank=True)
    specificpath = models.TextField(db_column=u'specificPath', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'AlbumRoots'
    def __unicode__(self):
        return self.label
        
class Album(models.Model):
    id = models.AutoField(primary_key=True)
    albumroot = models.ForeignKey(AlbumRoot, db_column=u'albumRoot') # Field name made lowercase.
    relativepath = models.TextField(db_column=u'relativePath') # Field name made lowercase.
    date = models.DateField(null=True, blank=True)
    caption = models.TextField(blank=True)
    collection = models.TextField(blank=True)
    icon = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'Albums'
    def __unicode__(self):
        return self.relativepath
    def getCover(self):
        "Returns Image ID of Cover for the album."
        url = ''
        images = self.image_set.all()
        for image in images:
            try:
                url = image.getUrl()
            except IndexError:
                url = ''
            if (url != ''):
                return image.id
        return 0

class DownloadHistory(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    identifier = models.TextField(blank=True)
    filename = models.TextField(blank=True)
    filesize = models.IntegerField(null=True, blank=True)
    filedate = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'DownloadHistory'

class ImageComments(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    imageid = models.IntegerField(null=True, blank=True)
    type = models.IntegerField(null=True, blank=True)
    language = models.TextField(blank=True)
    author = models.TextField(blank=True)
    date = models.DateTimeField(null=True, blank=True)
    comment = models.TextField(blank=True)
    class Meta:
        db_table = u'ImageComments'

class ImageCopyright(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    imageid = models.IntegerField(null=True, blank=True)
    property = models.TextField(blank=True)
    value = models.TextField(blank=True)
    extravalue = models.TextField(db_column=u'extraValue', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ImageCopyright'

class ImageHaarmatrix(models.Model):
    imageid = models.IntegerField(primary_key=True, blank=True) # TODO(chs): foreign_key ?
    modificationdate = models.DateTimeField(null=True, db_column=u'modificationDate', blank=True) # Field name made lowercase.
    uniquehash = models.TextField(db_column=u'uniqueHash', blank=True) # Field name made lowercase.
    matrix = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'ImageHaarMatrix'

class ImageHistory(models.Model):
    imageid = models.IntegerField(primary_key=True, blank=True) # TODO(chs): foreign_key?
    uuid = models.TextField(blank=True)
    history = models.TextField(blank=True)
    class Meta:
        db_table = u'ImageHistory'

class ImageInformation(models.Model):
    imageid = models.IntegerField(primary_key=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    creationdate = models.DateTimeField(null=True, db_column=u'creationDate', blank=True) # Field name made lowercase.
    digitizationdate = models.DateTimeField(null=True, db_column=u'digitizationDate', blank=True) # Field name made lowercase.
    orientation = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    format = models.TextField(blank=True)
    colordepth = models.IntegerField(null=True, db_column=u'colorDepth', blank=True) # Field name made lowercase.
    colormodel = models.IntegerField(null=True, db_column=u'colorModel', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ImageInformation'

class ImageMetadata(models.Model):
    imageid = models.IntegerField(primary_key=True, blank=True)
    make = models.TextField(blank=True)
    model = models.TextField(blank=True)
    lens = models.TextField(blank=True)
    aperture = models.FloatField(null=True, blank=True)
    focallength = models.FloatField(null=True, db_column=u'focalLength', blank=True) # Field name made lowercase.
    focallength35 = models.FloatField(null=True, db_column=u'focalLength35', blank=True) # Field name made lowercase.
    exposuretime = models.FloatField(null=True, db_column=u'exposureTime', blank=True) # Field name made lowercase.
    exposureprogram = models.IntegerField(null=True, db_column=u'exposureProgram', blank=True) # Field name made lowercase.
    exposuremode = models.IntegerField(null=True, db_column=u'exposureMode', blank=True) # Field name made lowercase.
    sensitivity = models.IntegerField(null=True, blank=True)
    flash = models.IntegerField(null=True, blank=True)
    whitebalance = models.IntegerField(null=True, db_column=u'whiteBalance', blank=True) # Field name made lowercase.
    whitebalancecolortemperature = models.IntegerField(null=True, db_column=u'whiteBalanceColorTemperature', blank=True) # Field name made lowercase.
    meteringmode = models.IntegerField(null=True, db_column=u'meteringMode', blank=True) # Field name made lowercase.
    subjectdistance = models.FloatField(null=True, db_column=u'subjectDistance', blank=True) # Field name made lowercase.
    subjectdistancecategory = models.IntegerField(null=True, db_column=u'subjectDistanceCategory', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ImageMetadata'

class ImagePositions(models.Model):
    imageid = models.IntegerField(primary_key=True, blank=True)
    latitude = models.TextField(blank=True)
    latitudenumber = models.FloatField(null=True, db_column=u'latitudeNumber', blank=True) # Field name made lowercase.
    longitude = models.TextField(blank=True)
    longitudenumber = models.FloatField(null=True, db_column=u'longitudeNumber', blank=True) # Field name made lowercase.
    altitude = models.FloatField(null=True, blank=True)
    orientation = models.FloatField(null=True, blank=True)
    tilt = models.FloatField(null=True, blank=True)
    roll = models.FloatField(null=True, blank=True)
    accuracy = models.FloatField(null=True, blank=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = u'ImagePositions'

class ImageProperties(models.Model):
    imageid = models.IntegerField(primary_key=True)
    property = models.TextField()
    value = models.TextField()
    class Meta:
        db_table = u'ImageProperties'

class ImageRelations(models.Model):
    subject = models.IntegerField(blank=True, primary_key=True)
    object = models.IntegerField(null=True, blank=True)
    type = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'ImageRelations'

class ImageTagPoperties(models.Model):
    imageid = models.IntegerField(blank=True, primary_key=True)
    tagid = models.IntegerField(null=True, blank=True)
    property = models.TextField(blank=True)
    value = models.TextField(blank=True)
    class Meta:
        db_table = u'ImageTagProperties'

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album, null=True, blank=True, db_column=u'album')
    name = models.CharField(max_length=200)
    status = models.IntegerField()
    category = models.IntegerField()
    #modificationdate = models.DateTimeField(null=True, db_column=u'modificationDate', blank=True) # TODO include this again (causes parsing error)
    filesize = models.IntegerField(null=True, db_column=u'fileSize', blank=True) # Field name made lowercase.
    uniquehash = models.CharField(max_length=200, db_column=u'uniqueHash', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Images'
    def __unicode__(self):
        return self.name
    def getUrl(self):
        url = settings.PHOTO_URL
        url += self.album.albumroot.specificpath
        url += self.album.relativepath + '/'  + self.name
        name, ext = os.path.splitext(self.name)
        # GIMP XCF files are not supported.
        if (ext == '.xcf'):
          return ''
        return sanitise(url)

class ImageTag(models.Model):
    image = models.ForeignKey("Image", db_column=u'imageid')
    tag = models.ForeignKey("Tag", db_column=u'tagid')
    class Meta:
        db_table = u'ImageTags'
        unique_together = ('image', 'tag')
    def __unicode__(self):
      return u"Image: %s --> Tag: %s" % (self.image, self.tag)

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    usage_count = models.IntegerField(null=True, blank=True, db_column=u'pid')
    name = models.TextField()
    icon = models.IntegerField(null=True, blank=True)
    iconkde = models.TextField(blank=True)
    images = models.ManyToManyField(Image, through=ImageTag)
    class Meta:
        db_table = u'Tags'
    def get_images(self):
        return self.images.all()

class Searches(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    type = models.IntegerField(null=True, blank=True)
    name = models.TextField()
    query = models.TextField()
    class Meta:
        db_table = u'Searches'

class Settings(models.Model):
    keyword = models.TextField(unique=True, primary_key=True)
    value = models.TextField(blank=True)
    class Meta:
        db_table = u'Settings'

class TagProperties(models.Model):
    tagid = models.IntegerField(blank=True, primary_key=True)
    property = models.TextField(blank=True)
    value = models.TextField(blank=True)
    class Meta:
        db_table = u'TagProperties'

class TagsTree(models.Model):
    id = models.IntegerField(primary_key=True)
    pid = models.IntegerField()
    class Meta:
        db_table = u'TagsTree'
