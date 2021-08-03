#!/usr/bin/node
const myArray = [];
let i = 0;
let j = 2;
let sorted = [];

if (process.argv.length < 4) {
  console.log(0);
} else {
  for (; i < (process.argv.length - 2); i++) {
    myArray[i] = parseInt(process.argv[j]);
    j++;
  }
}
sorted = myArray.sort((myArray, b) => (b - myArray));
console.log(sorted[1]);
