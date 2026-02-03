import sys
from stats import get_book_txt, get_char_freq, get_num_words, sort_chars # noqa: F401

def main():

    try:
        path_to_book = sys.argv[1]
    except IndexError:
        print("missing path/to/book argument!")
        sys.exit(1)


    print("==========BOOK BOT==========")

    print(f"Analyzing book found at {path_to_book}...")
    
    get_book_txt(path_to_book)
    
    print("----------Word Count----------")
    
    get_num_words(path_to_book)
    
    print("----------Character Count----------")
    
    sort_chars(path_to_book)




if __name__ == "__main__":
    main()
