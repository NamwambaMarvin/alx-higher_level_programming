#!/usr/bin/node
// Class that defines a Rectangle with width and height

module.exports = class Rectangle {
	constructor (w, h) {
		if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}
};
