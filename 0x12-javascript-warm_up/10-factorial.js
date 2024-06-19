#!/usr/bin/node

const arg = parseInt(process.argv[2]);

if (Number.isNaN(arg)) {
  console.log(1);
} else {
  let result = 1;
  for (let i = arg; i > 0; --i) {
    result *= i;
  }
  console.log(result);
}
