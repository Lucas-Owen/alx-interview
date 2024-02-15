#!/usr/bin/node
const request = require('request');
const argv = require('process').argv;

function getCharacterList () {
  return new Promise((resolve, reject) => {
    const movieId = argv[2];
    request(
      {
        url: `https://swapi-api.alx-tools.com/api/films/${movieId}`,
        method: 'GET'
      }, (err, res, body) => {
        if (err || res.statusCode !== 200) { reject(err); }
        resolve(JSON.parse(body).characters);
      });
  });
}

function getCharacterNames (characters) {
  const characterNames = characters.map(character =>
    new Promise((resolve, reject) => {
      request({
        url: character,
        method: 'GET'
      }, (err, res, body) => {
        if (err || res.statusCode !== 200) { reject(err); }
        resolve(JSON.parse(body).name);
      });
    }));
  return Promise.all(characterNames);
}

async function main () {
  const characters = await getCharacterList();
  const names = await getCharacterNames(characters);
  names.forEach(name => console.log(name));
}

main();
