import sys

def get_book_text(filepath):
    path = f"{filepath}"
    with open(path, encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents

from stats import word_count, get_chars_dict, chars_dict_to_sorted_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    path_file = get_book_text(book_path)
    num_words = word_count(path_file)
    chars_dict = get_chars_dict(path_file)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(path_file, num_words, chars_sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(path_file, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()