# Python Async Comprehension

This project focuses on asynchronous comprehensions and generators in Python, building on the concepts of async/await syntax.

## Learning Objectives

- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Tasks

0. **Async Generator**: Writing a coroutine called `async_generator` that yields a random number between 0 and 10 after waiting 1 second, 10 times.

1. **Async Comprehensions**: Writing a coroutine called `async_comprehension` that collects 10 random numbers using an async comprehension over the `async_generator` function.

2. **Run Time for Four Parallel Comprehensions**: Writing a function called `measure_runtime` that executes `async_comprehension` four times in parallel and measures the total runtime.

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A README.md file at the root of the project folder is mandatory
- Your code should use the pycodestyle style (version 2.5.*)
- All your files must be executable
- All your modules should have documentation
- All your functions should have documentation
- All your functions and coroutines must be type-annotated