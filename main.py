import sys

from stats import word_count
from stats import chars
from stats import dict_sort
from stats import char_list

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

def get_book_text(filepath):
    book_text = ""
    with open(filepath) as f:
        book_text = f.read()
    return book_text
def main():
    book = get_book_text(path)
    return book

full_text = main()
character_count = chars(full_text)

num_words = word_count(full_text)
num_chars = chars(full_text)
sorted_chars = dict_sort(num_chars)


print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")
char_list(sorted_chars)
print("============= END ===============")