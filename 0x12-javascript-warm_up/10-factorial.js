#!/usr/bin/node

const arg = parseInt(process.argv[2]);

if (Number.isNaN(arg)) {
  console.log(1);
} else {
  function factorial (arg) {
    if (arg > 0) {
      return (arg * factorial(arg - 1));
	}
    return 1;
  }
  console.log(factorial(arg));
}

