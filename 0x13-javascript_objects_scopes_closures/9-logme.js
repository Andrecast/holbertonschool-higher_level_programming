#!/usr/bin/node
let alreadyPrint = 0;
exports.logMe = function (item) {
  console.log(alreadyPrint + ': ' + item);
  alreadyPrint++;
};
