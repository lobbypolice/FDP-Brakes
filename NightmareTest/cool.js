const Nightmare = require('nightmare')
const nightmare = Nightmare({ 
    show: true, 
    waitTimeout: 100000 // in ms
})
nightmare
  .goto('http://yahoo.com')
  .type('input[title="Search"]', 'github nightmare')
  .click('.searchsubmit');