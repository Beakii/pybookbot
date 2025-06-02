from stats import *

def get_book_text():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def main():
    num_words = count_words(get_book_text())
    num_letters = analyze_text(get_book_text())

    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    format_output(num_letters)
    print("============= END ===============")


main()
