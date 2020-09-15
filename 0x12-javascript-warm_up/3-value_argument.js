#!/usr/bin/node
// Script that prints the first argument passed to it

if (process.argv.length <= 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
