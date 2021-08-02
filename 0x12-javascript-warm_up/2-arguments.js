#!/usr/bin/node
const _arguments = process.argv.length;
if (_arguments === 2) {
  console.log('No argument');
} else if (_arguments === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
