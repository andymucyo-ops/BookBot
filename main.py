
def get_book_txt() -> str:
    with open("./books/frankenstein.txt", "r") as f:
        file_content = f.read() 
        
        return file_content


def get_num_words() -> None:
    list_words: list[str] = get_book_txt().split()

    num_words: int = len(list_words)

    print(f"Found {num_words} total words")



def main():

    get_book_txt()

    # print(get_book_txt())

    get_num_words()


if __name__ == "__main__":
    main()
