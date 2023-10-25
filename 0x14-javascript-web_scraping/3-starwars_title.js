#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/:id'.concat(argv[2]);

request(url, function(_err, _err, body){
	body = JSON.parse(body);
	console.log(body.title);
});
