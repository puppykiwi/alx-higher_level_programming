#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i !== this.height; i++) {
      let s = '';
      for (let j = 0; j !== this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }

  rotate () {
    const tmpw = this.width;
    const tmph = this.height;
    this.height = tmpw;
    this.width = tmph;
  }

  double () {
    this.width = (this.width * 2);
    this.height = (this.height * 2);
  }
}

module.exports = Rectangle;
