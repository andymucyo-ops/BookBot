def get_book_txt() -> str:
    #return whole book content as a string
    with open("./books/frankenstein.txt", "r") as f:
        file_content = f.read() 
        
        return file_content


def get_num_words() -> None:
    #prints number of words in the book
    list_words: list[str] = get_book_txt().split()

    num_words: int = len(list_words)

    print(f"Found {num_words} total words")


def get_char_freq() -> dict[str,int]:
    #retruns dictionnary with character occurence

    full_txt: str = get_book_txt().lower()
    print(full_txt[:5])

    char_freq: dict[str,int] = {}

    for char in full_txt:
        # print(char)
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1

    return char_freq


if __name__ == "__main__":

    get_book_txt()
    get_num_words()
    print(get_char_freq())
