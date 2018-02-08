const Nightmare = require('nightmare')
Nightmare()
    .goto('https://news.ycombinator.com/')
    .evaluate(() => document.querySelector('.storylink').innerText)
    .end()
    .then(result => {
        console.log(`The top news story on Hacker News currently is:\n${result}`)
    })
    .catch(error => console.error(error))