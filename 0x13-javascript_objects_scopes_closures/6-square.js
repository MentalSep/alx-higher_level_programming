#!/usr/bin/node

const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      console.log(c ? c.repeat(this.height) : 'X'.repeat(this.height));
    }
  }
}

module.exports = Square;
