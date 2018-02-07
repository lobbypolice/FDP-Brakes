//runs with errors

var page = new WebPage();
page.open('http://www.espn.com', function (status) {
    page.render('fb.png');
    phantom.exit();
});
