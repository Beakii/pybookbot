def count_words(book_text: str):
    words = book_text.split()
    return len(words)

def analyze_text(book_text: str):
    book_text = book_text.lower()
    book_words = book_text.split()
    book_string = ""
    book_analysis = {}

    for word in book_words:
        book_string += word

    for letter in book_string:
        i = 0

        if letter not in book_analysis:
            book_analysis[letter] = 1
        else:
            book_analysis[letter] = book_analysis[letter] + 1

        i += 1

    return book_analysis


def format_output(letter_dict: dict[str,int]) -> None:
    sorted_dict = sorted(letter_dict.items(), key=lambda item: item[1], reverse=True)

    for letter, count in sorted_dict:
        if letter.isalpha():
            print(f"{letter}: {count}")