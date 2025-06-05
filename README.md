# PyBookBot

**PyBookBot** is a command-line Python application designed to process and analyze text from `.txt` files, such as ebooks. It counts word occurrences and provides simple analytics such as the most frequent words in the text. This project focuses on foundational Python programming concepts, emphasizing text processing, data structures, and clean code design.

## Features

- Loads plain-text files (`.txt`) for analysis
- Cleans and normalizes text input
- Counts frequency of each word

## Key Concepts Learned

* **File I/O**: Reading and validating plain-text files from the filesystem.
* **String Manipulation**: Cleaning and formatting text by removing punctuation and standardizing to lowercase.
* **Data Structures**:
  * Lists for storing tokens
  * Dictionaries for word counts
  * Tuples for sorting word-frequency pairs
* **Modular Code Design**: Organizing functionality into functions to improve readability and maintainability.
* **Basic CLI Interaction**: Using `sys.argv` to allow command-line argument inputs.
* **Error Handling**: Using `try/except` blocks to manage file access issues and ensure a smooth user experience.
* **Sorting and Lambda Functions**: Leveraging Python's built-in `sorted()` and `lambda` for ranking word frequencies.

## Getting Started

### Prerequisites

* Python 3.7 or higher

### Installation

Clone the repository:

```bash
git clone https://github.com/Beakii/pybookbot.git
cd pybookbot
```

### Running the Script

```bash
python pybookbot.py <path-to-text-file>
```

For example:

```bash
python pybookbot.py books/alice_in_wonderland.txt
```

**Note**: This project was built as a learning tool to solidify core Python programming skills.
