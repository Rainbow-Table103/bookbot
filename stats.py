def word_count(full_text):
    words = full_text.split()
    num_words = len(words)
    return num_words
    
def chars(full_text):
    char_count = {}
    for character in full_text:
        lower_char = character.lower()
        if lower_char not in char_count:
            char_count[lower_char] = 0
        char_count[lower_char] += 1
    return char_count

def sort_on(items):
    return items["num"]

def dict_sort(dictonary):
    sorted = []
    for l in dictonary:
        sorted.append({"char": l, "num": dictonary[l]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

def char_list(sc):
    for i in sc:
        current = i
        if current["char"].isalpha():
            print(f"{current["char"]}: {current["num"]}")