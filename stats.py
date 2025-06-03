## Counts number of words in text
def get_num_words(book_text):
    num_words = len(book_text.split())
    return num_words


## Counts number of each letter in text
def get_num_char(book_text):
    book_text = book_text.lower()
    char_count = {}

    for char in book_text:
        if char in char_count:
            char_count[char] += 1

        else:
            char_count[char] = 1
        
    return char_count
    

## Creates report of character counts in desc order
def sorted_char_count(char_count_dict):
    char_list = []

    for char, count in char_count_dict.items():
        if char.isalpha():     ## Only includes alphabet chars
            char_list.append({"char": char, "num": count})
    
    def sort_on(d):
        return d["num"]

    char_list.sort(reverse=True, key=sort_on)
    
    
    return char_list