#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  // method prints put the shape of the rectangle
  print () {
    let i = 0;
    let u = 0;
    let row = '';
    for (i = 0; i < this.width; i++) {
      row += 'X';
    }
    for (u = 0; u < this.height; u++) {
      console.log(row);
    }
  }
}
module.exports = Rectangle;