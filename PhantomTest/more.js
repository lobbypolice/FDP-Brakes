var page = require('webpage').create();
page.settings.userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
page.viewportSize = {
    width: 1280,
    height: 1024
}
page.open('http://detectmybrowser.com/', function (status) {
    console.log("Status: " + status);
    if (status === "success") {
        page.render('example.png');

    }
    phantom.exit();
});
