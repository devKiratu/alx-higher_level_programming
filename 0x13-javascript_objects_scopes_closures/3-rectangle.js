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

  print () {
    for (let i = 0; i < this.height; i++) {
      let pattern = '';
      for (let j = 0; j < this.width; j++) {
        pattern += 'X';
      }
      console.log(pattern);
    }
  }
}

module.exports = Rectangle;
