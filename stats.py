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

    char_freq: dict[str,int] = {}

    for char in full_txt:
        # print(char)
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1

    return char_freq


def sort_chars() -> None: 
    #sorts characters by highest frequency and prints them
    char_freq: dict[str,int] = get_char_freq()

    sorted_char_freq: dict[str,int] = dict(sorted(char_freq.items(), key=lambda item: item[1], reverse = True))
   

    char_list = [char for char in sorted_char_freq]
    # print(f"char_list: {char_list}")

    num_list = [sorted_char_freq[char] for char in sorted_char_freq]
    # print(f"num_list: {num_list}")
    
    
    sorted_char_freq_list: list = []
    for i in range(0,len(char_list)):
        sorted_char_freq_list.append(dict(char = char_list[i] , num = num_list[i]))
    # print(sorted_char_freq)
    
    #exclude non-alphabetical characters from final print
    for i in range(0,len(sorted_char_freq_list)):
        if sorted_char_freq_list[i]['char'].isalpha():
            print(f"'{sorted_char_freq_list[i]['char']}': {sorted_char_freq_list[i]['num']}")


    
    

if __name__ == "__main__":
    
    # get_book_txt()
    # get_num_words()
    # get_char_freq()
    sort_chars()
