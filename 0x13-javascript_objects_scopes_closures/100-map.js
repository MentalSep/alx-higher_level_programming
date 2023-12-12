#!/usr/bin/node

const list = require('./100-data').list;
console.log(list);
const newlist = list.map((x, index) => x * index);
console.log(newlist);
