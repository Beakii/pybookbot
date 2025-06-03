from stats import *
from sys import argv, exit

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(argv) > 1:
        num_words = count_words(get_book_text(argv[1]))
        num_letters = analyze_text(get_book_text(argv[1]))
    
        print("============ BOOKBOT ============")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        format_output(num_letters)
        print("============= END ===============")
    else:
        print('Usage: python3 main.py <path_to_book>')
        exit(1)

main()
