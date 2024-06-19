#!/usr/bin/node

const argv = process.argv.slice(2);

if (argv.length) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
