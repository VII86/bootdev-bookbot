def count_words(book_content):
    words = book_content.split()
    return len(words)



def count_letters(book_content):
    lower_content = book_content.lower()
    letters = []
    for letter in lower_content:
        if not letter.isalpha():
            continue
        found = False
        for entry in letters:
            if entry["char"]==letter:
                entry["num"] += 1
                found = True
                break
        if not found:
            letters.append({"char":letter, "num": 1})
                
    return letters