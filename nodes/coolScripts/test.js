<<<<<<< HEAD
function getData(name, screenshot) {
    const puppeteer = require('puppeteer');
    const devices = require('puppeteer/DeviceDescriptors');
    console.log(name + "This is working")
    (async () => {
        const browser = await puppeteer.launch({headless: false});
        const page = await browser.newPage();
        await page.goto(name);
        await page.waitForNavigation();
        await page.screenshot({path: screenshot});
        await browser.close();
    })();
}
document.getElementById('autozone').onclick = function(){
    getData("https://www.autozone.com/", "autozone.png");
}
document.getElementById('advancedAuto').onclick = function(){
    getData("https://shop.advanceautoparts.com/", "advancedauto.png");
}
document.getElementById('orielly').onclick = function(){
    getData("https://www.oreillyauto.com/", "orielly.png");
} 
document.getElementById('napa').onclick  = function(){
    getData("https://www.napaonline.com/", "napa.png");
} 
document.getElementById('pepboys').onclick = function(){
    getData("https://www.pepboys.com/", "pepboys.png");
} 
=======
"use strict";
var csv = require("csv-query");
 
 
csv.createFromFile(
  __dirname + "/Advanced.csv"
).then(function (db) {
  return db.findOne({ 
    modelNumber: "#GNAD785" 
  });
}).then(function (record) {
  return record;
}).catch(function (error) {
  throw error;
});
>>>>>>> f1788c3b240da2380fba714f1e87e4112800e50e
