#!/usr/bin/node
// Arguments
const lenArgv = process.argv.length;

if (lenArgv <= 2) {
  console.log('No argument');
} else if (lenArgv === 3) {
  console.log('Argument found');
} else if (lenArgv > 3) {
  console.log('Argument found');
}
