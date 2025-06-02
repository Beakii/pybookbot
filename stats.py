def count_words(book_text):
    words = book_text.split()
    return len(words)

def analyze_text(book_text):
    book_text = book_text.lower()
    book_letters = book_text.split()
    book_analysis = {}

    for i in range(0, len(letters)):
        counter = 0
        for j in range(0, len(book_text)):
            if book_text[]