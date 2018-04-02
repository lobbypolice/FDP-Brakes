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