#!/usr/bin/node

const SquareF = require('./5-square');

class Square extends SquareF {
  charPrint (c) {
    for (let i = 0; i < this.height; ++i) {
      console.log(c ? c.repeat(this.width) : 'X'.repeat(this.width));
    }
  }
}

module.exports = Square;
