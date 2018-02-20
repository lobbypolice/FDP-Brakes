const Nightmare = require('nightmare')
const nightmare = Nightmare({ 
    show: true, 
    waitTimeout: 100000 // in ms
})
nightmare
    .goto("https://www.pepboys.com/")
    .wait(2000)