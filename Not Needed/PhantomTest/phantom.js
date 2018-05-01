var page = require('webpage').create();
var url = 'https://www.joecolantonio.com/';
page.open(url, function (status) {
    console.log(status);
    phantom.exit();
});
