#!/usr/bin/node

const reps = parseInt(process.argv[2]);
if (isNaN(reps)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < reps; i++) {
    console.log('C is fun');
  }
}
