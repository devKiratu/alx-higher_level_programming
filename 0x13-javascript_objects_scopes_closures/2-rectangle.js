#!/usr/bin/node

class Rectangle {
  width;
  height;

  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
