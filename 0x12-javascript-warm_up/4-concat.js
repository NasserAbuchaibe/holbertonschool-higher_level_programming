#!/usr/bin/node
// script that prints two arguments passed to it
const lenArgv = process.argv.length;
if (lenArgv <= 2) {
  console.log('undefined is undefined');
} else if (lenArgv === 4) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else if (lenArgv === 3) {
  console.log(process.argv[2] + ' is undefined');
}
