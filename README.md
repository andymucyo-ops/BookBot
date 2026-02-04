# bookbot

BookBot [Boot.dev](https://www.boot.dev) project!

Here is a simple CLI tool to analyise word count and character occurence in books.

### requirment

python3 [download python](https://www.python.org/downloads/)

### How to run it

- clone this repo: ```{bash} git clone https://github.com/andymucyo-ops/BookBot```

- create a books directory ```{bash} mkdir books```

- download a few books to try the CLI tool on:

    ```{bash}
    wget -O books/frankenstein.txt https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/frankenstein.txt

    wget -O books/mobydick.txt https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/mobydick.txt
    
    wget -O books/prideandprejudice.txt https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/prideandprejudice.txt
   ```
- run as follows, from project root: ```{bash} python3 main.py <path_to_book>```
