import sys
from stats import count_words, count_letters

def get_book_text(myPath):
    file_contents = ""
    with open(myPath) as f:
        file_contents = f.read()
    return file_contents

def sort_on(items):
    return items["num"]

def report(path):
    print(f'============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print(f'----------- Word Count ----------')
    print(f'Found {count_words(get_book_text(path))} total words')
    print(f'--------- Character Count -------')
    lettercounts = count_letters(get_book_text(path))
    lettercounts.sort(reverse=True,key=sort_on)
    for item in lettercounts:
        print(f'{item["char"]}: {item["num"]}')
    print(f'============= END ===============')    

def __main__():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    report(sys.argv[1])

__main__()