// Copyright 2013 Christoph Siedentop <digikamweb@siedentop.name>
$(document).ready(function(){
  loadAlbums('latestAlbums.json');
  // Connect Reset Button
  $('#album_reset').click(function() { loadAlbums('latestAlbums.json') });
});

// Load Albums behind given url. For example latestAlbums.json
function loadAlbums(url) {
  $('#gallery').html("");
  $.getJSON(url, function(data) {
    $.each(data.albums, function(id, album) {
      // Generate or Load Thumbnail for album
      var img = $("<img/>")
      $('#gallery').append(img);
      $.getJSON('thumbnail/' + album.coverId +  '/100', function (thumbnail) {
        if ('url' in thumbnail) {
          img.attr('src', thumbnail.url);
        } else {
          img.attr('src', 'http://localhost:8081/no_preview.jpg').attr('width', '100px');
        }
        img.data('album', album.id).click(function() { openAlbum(album.id); });
      });
    });
  });
}

// Open Album with given Album ID
function openAlbum(id) {
  $('#gallery').html('');
  $.getJSON('album/' + id + '.json', function(data) {
    $.each(data.images, function(i, image) {
      var img = $("<img/>");
      $('#gallery').append(img);
      $.getJSON('thumbnail/' + image + '/640', function (thumbnail) {
        if ('url' in thumbnail) {
          img.attr('src', thumbnail.url);
        } else {
          img.attr("src", "http://localhost:8081/no_preview.jpg");
        }
      });
    });
  });
}
