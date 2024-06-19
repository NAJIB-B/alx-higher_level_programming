#!/usr/bin/node

const arg = parseInt(process.argv[2]);

if (Number.isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; ++i) {
    const val = 'X'.repeat(arg);
    console.log(val);
  }
}
