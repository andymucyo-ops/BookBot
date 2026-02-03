def main():
    def get_book_txt():
        with open("./books/frankenstein.txt", "r") as f:
            file_content = f.read() 
            
            return file_content

    print(get_book_txt())

if __name__ == "__main__":
    main()
