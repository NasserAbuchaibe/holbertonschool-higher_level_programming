#!/usr/bin/node

const fs = require('fs');

const f1 = fs.readFileSync(process.argv[2], 'utf8');
const f2 = fs.readFileSync(process.argv[3], 'utf8');
const f3 = f1 + f2;

fs.writeFileSync(process.argv[4], f3);
