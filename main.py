def get_book_text(filepath):
    path = f"{filepath}"
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    path_file = get_book_text("books/frankenstein.txt")
    return print(path_file)

main()