#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { // sólo si w y h son positivos cree los objetos
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
