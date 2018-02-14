const Nightmare = require('nightmare')
const nightmare = Nightmare({ 
    show: true, 
    waitTimeout: 100000 // in ms
})

nightmare
    .goto('https://www.autozone.com/')
    .wait(200000)
    .click('ul#mainNav > li:nth-child(1) > ul:nth-child(3) > li:nth-child(1) > div.megaNav:nth-child(2) > div.grid-24.clearfix.flush:nth-child(1) > div.grid-16.flush:nth-child(1) > div.grid-12.clearfix.popCats:nth-child(4) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)')
    .wait(2000)
    .end()
    
    .then(function (result) {
        console.log(result)
    })
    .catch(function (error) {
        console.error('Error:', error);
    });
