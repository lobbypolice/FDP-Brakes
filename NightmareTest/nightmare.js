const Nightmare = require('nightmare')
const nightmare = Nightmare({ 
    show: true, 
    waitTimeout: 100000 // in ms
})
nightmare
    .goto('https://news.ycombinator.com/')
    .wait(2000)
    .evaluate(() => document.querySelector('.storylink').innerText)
    .end()
    .then(result => {
        console.log(`The top news story on Hacker News currently is:\n${result}`)
    })
    .catch(error => console.error(error))