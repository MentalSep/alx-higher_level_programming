#!/usr/bin/node

if (process.argv.length > 3) {
  let numbers = process.argv.slice(2).map(Number);
  let maxNum = Math.max(...numbers);

  numbers = numbers.filter(num => num !== maxNum);
  maxNum = Math.max(...numbers);
  console.log(maxNum);
} else {
  console.log('0');
}
