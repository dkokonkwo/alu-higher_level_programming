// #!/usr/bin/node
const twoSquare = require('./5-square');
class Square extends twoSquare {
  charPrint (c = 'X') {
    //  method prints a rectangle with a letter
    let i = 0;
    let row = '';
    for (i = 0; i < this.width; i++) {
      row += c;
    }
    for (i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

const s1 = new Square(4);
s1.charPrint();

s1.charPrint('C');