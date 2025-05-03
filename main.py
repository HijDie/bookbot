import sys
# check if the user gives 2 arguments when running the program
# instead of hardcoding book path use sys.argv[1] to give the second argument as path
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# importing functions from a diffrent file
from stats import count_words
from stats import count_chars
from stats import chars_dict_to_sorted_list

# get the text from the file
def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    book_text = get_book_text(f"{sys.argv[1]}")

    word_count = count_words(book_text)
    char_count = count_chars(book_text)
    sorted_list = chars_dict_to_sorted_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    # looping over every dict in the list
    for char_dict in sorted_list:
        character = char_dict["char"]
        count = char_dict["num"]
        if character.isalpha():
            print(f"{character}: {count}")
    
main()