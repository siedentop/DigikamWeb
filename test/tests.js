test( "hello test", function() {
ok( 1 == "1", "Passed!" );
});


function saysHi(name) {
    return "Hi, " + name;
};

test('saysHi()', function() {
    equal(saysHi("Jack"), "Hi, Jack", "function outputs string correctly")
});

asyncTest("thumbnail AJAX", function() {
  
  thumbnail.query(function(res) {
    ok(res, "AJAX call got a result");
    ok(res.url, "URL exists in response");
    equal(res.url,"http://localhost:8000/thumbnail.jpg", "URL returned is correct");
    equal(res.title, "Drainpipe", "The title returned is correct");
    start();
  });
});

test('setThumbnail()', function() {
});

test('getThumbnail()', function() {
  getThumbnail(''
});