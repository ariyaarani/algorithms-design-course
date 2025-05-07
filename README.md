
# Algorithms Design Course

This repository contains a collection of basic algorithm implementations in Python. It is intended as a resource for students and beginners who are learning the fundamentals of programming and algorithm design. Each algorithm is implemented with a focus on simplicity, readability, and educational value.

## Overview

The repository includes the following algorithm categories:

### Binary Search
- Implements the classic binary search algorithm.
- Searches for an element in a sorted list by repeatedly dividing the search interval in half.
- Efficient in terms of time complexity: O(log n).
- Suitable for understanding divide-and-conquer strategies.

### Bubble Sort
- Implements the bubble sort algorithm.
- Sorts a list by repeatedly swapping adjacent elements that are out of order.
- One of the simplest sorting algorithms, used to teach basic sorting concepts.
- Time complexity: O(n²), best used for small datasets.

### Merge Sort
- Implements the merge sort algorithm.
- Uses a divide-and-conquer approach to sort elements by recursively dividing the list and then merging the sorted halves.
- More efficient than bubble sort for larger datasets.
- Time complexity: O(n log n).

### Name Splitting
- A simple utility to split full names into components such as first name and last name.
- Demonstrates basic string manipulation and input/output operations in Python.
- Useful for beginner practice and understanding basic text parsing.

## Project Structure

The repository is organized as follows:

```
algorithms-design-course/
│
├── binary_search/
│   └── src/
│       └── binary_search.py
│
├── bubble_search/
│   └── src/
│       └── bubble_sort.py
│
├── merge_sort/
│   └── src/
│       └── merge_sort.py
│
├── name_splitting/
│   └── src/
│       └── name_splitting.py
│
├── .gitignore
└── README.md
```

Each algorithm resides in its own folder under a `src/` subdirectory to keep the code organized and modular.

## Getting Started

### Prerequisites

- Python 3.7 or higher must be installed on your system.

### Running the Scripts

You can run any algorithm by navigating to the appropriate directory and executing the Python script. For example:

```bash
cd bubble_search/src
python bubble_sort.py
```

Repeat the same process for the other scripts.

## Educational Purpose

This repository is intended primarily for educational purposes, including:

- Practicing and understanding fundamental algorithms.
- Learning core programming constructs such as loops, conditionals, functions, and recursion.
- Serving as sample code for programming assignments or introductory courses.

## Contributing

Contributions are welcome and appreciated. You can contribute in the following ways:

- Add new algorithms or data structures.
- Improve the readability or efficiency of existing code.
- Add comments or documentation for better understanding.

To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes.
4. Commit and push to your fork.
5. Open a Pull Request for review.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
