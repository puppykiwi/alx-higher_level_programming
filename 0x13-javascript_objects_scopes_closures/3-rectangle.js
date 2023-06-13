#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 || h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    console.log(this);
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; i < this.width; j++) {
        str += 'x';
      }
      console.log(str);
    }
  }
}

module.exports = Rectangle;

const r1 = new Rectangle(2, 3);
console.log(r1);
r1.print();
