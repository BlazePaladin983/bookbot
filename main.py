def get_book_text(filepath):
    path = f"{filepath}"
    with open(path, encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents

def word_count(book):
    words = len(book.split())
    return words

def main():
    path_file = get_book_text("books/frankenstein.txt")
    num_words = word_count(path_file)
    return print(f"{num_words} words found in the document")

main()