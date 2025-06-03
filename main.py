from stats import get_num_words, get_num_char, sorted_char_count
import sys

## Opens the file to read the contents
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)    ## Captures book text
    num_words = get_num_words(book_text)    ## Calls word num function
    num_char = get_num_char(book_text)     ## Calls char num function
    sorted_counts = sorted_char_count(num_char)    ## Calls sorted dict
    print(f"Found {num_words} total words")
    ## print(f"{num_char}")
    for item in sorted_counts:
        print(f"{item['char']}: {item['num']}")


if __name__ == "__main__":
    main()