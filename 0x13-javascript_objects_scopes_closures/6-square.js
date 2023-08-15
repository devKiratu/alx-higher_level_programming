#!/usr/bin/node

const ParentSquare = require('./5-square.js');

class Square extends ParentSquare {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let pattern = '';
      for (let j = 0; j < this.width; j++) {
        pattern += c;
      }
      console.log(pattern);
    }
  }
}

module.exports = Square;
