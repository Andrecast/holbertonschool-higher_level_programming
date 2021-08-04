#!/usr/bin/node
exports.converter = function (base) {
  return function (base10) {
    return base10.toString(base);
  };
};
