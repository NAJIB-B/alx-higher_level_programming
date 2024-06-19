#!/usr/bin/node

function add(a, b) {
  const val = a + b;
  console.log(val);
}

add(Number(process.argv[2]), Number(process.argv[3]));
