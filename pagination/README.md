# Pagination

This project focuses on implementing different pagination techniques in Python, including simple pagination, hypermedia pagination, and deletion-resilient pagination.

## Learning Objectives

- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Tasks

0. **Simple Helper Function**: Writing a function named `index_range` that takes two integer arguments `page` and `page_size` and returns a tuple containing the start and end index corresponding to the range of indexes to return in a list for those pagination parameters.

1. **Simple Pagination**: Implementing a `Server` class that paginates a database of popular baby names from a CSV file.

2. **Hypermedia Pagination**: Enhancing the `Server` class to provide hypermedia pagination with additional metadata.

3. **Deletion-Resilient Hypermedia Pagination**: Implementing a deletion-resilient version of the pagination that ensures consistency even when items are removed from the dataset between queries.

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