#!/usr/bin/node
function myFactorial (num) {
  if (!num) {
    return 1;
  } else {
    return num * myFactorial(num - 1);
  }
}
console.log(myFactorial(process.argv[2]));
