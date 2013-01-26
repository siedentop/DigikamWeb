# Copyright 2013 Christoph Siedentop <digikamweb@siedentop.name>
from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'digikam.views.index'),
    url(r'^album/(?P<album_id>\d+).json$', 'digikam.views.albumJson'),
    url(r'^thumbnail/(?P<image_id>\d+)/(?P<size>\d+)$', 'digikam.views.getThumbnail'),
    url(r'^tag/(?P<tag_id>\d+).json$', 'digikam.views.tagJson'),
    url(r'^latestAlbums.json$', 'digikam.views.latestAlbumsJson'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()