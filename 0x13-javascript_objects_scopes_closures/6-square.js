#!/usr/bin/node

// Inherits from the previous program

const OldSquare = require('./5-square');

module.exports = class Square extends OldSquare {
	constructor (size) {
		super (size, size);
	}
	double () {
		super.double();
	}
	charPrint (c = 'X') {
		super.print(c);
	}
}
