function getData(name, screenshot) {
    const puppeteer = require('puppeteer');
    const devices = require('puppeteer/DeviceDescriptors');

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