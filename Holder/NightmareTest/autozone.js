const Nightmare = require('nightmare')
//define a new Nightmare action named "clearCache"
Nightmare.action('clearCache',
  //define the action to run inside Electron
  function(name, options, parent, win, renderer, done) {
    //call the IPC parent's `respondTo` method for clearCache...
    parent.respondTo('clearCache', function(done) {
      //clear the session cache and call the action's `done`
      win.webContents.session.clearCache(done);
    });
    //call the action creation `done`
    done();
  },
  function(done) {
    //use the IPC child's `call` to call the action added to the Electron instance
    this.child.call('clearCache', done);
  });
const nightmare = Nightmare({ 
    show: true, 
    waitTimeout: 100000 // in ms
})

nightmare
    .useragent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36')
    .goto('https://www.autozone.com/')
    .wait(20000)
    .click('ul#mainNav > li:nth-child(1) > ul:nth-child(3) > li:nth-child(1) > div.megaNav:nth-child(2) > div.grid-24.clearfix.flush:nth-child(1) > div.grid-16.flush:nth-child(1) > div.grid-12.clearfix.popCats:nth-child(4) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)')
    .wait(2000)
    .end()
    
    .then(function (result) {
        console.log(result)
    })
    .catch(function (error) {
        console.error('Error:', error);
    });
