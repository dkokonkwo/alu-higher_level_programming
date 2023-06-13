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
  // swaps width with height
  rotate () {
    const holder = this.height;
    this.height = this.width;
    this.width = holder;
  }
  // doubles the width and height
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;