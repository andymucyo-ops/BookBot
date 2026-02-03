from stats import get_book_txt, get_char_freq, get_num_words, sort_chars # noqa: F401

def main():
    # get_book_txt()
    # # print(get_book_txt())
    # get_num_words()
    # print("---------------------------")
    # print(get_char_freq())
    print("==========BOOK BOT==========")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------Word Count----------")
    get_num_words()
    print("----------Character Count----------")
    sort_chars()




if __name__ == "__main__":
    main()
