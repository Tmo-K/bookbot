def main():
    path_to_file = "books/frankenstein.txt"
    file = read_file(path_to_file)
    words = count_words(file)
    characters = count_characters(file)
    report(path_to_file, words, characters)


def read_file(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
    return file_content

def count_words(file_content):
    words = file_content.split()
    word_count = len(words)
    return word_count

def count_characters(file_conent):
    alphabet = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, }
    file_conent = file_conent.lower()
    for i in alphabet:
        alphabet[i] = file_conent.count(i)
    return alphabet

def report(file, words, characters):
    print(f"--- Begin report of {file} ---")
    print(f"{words} words found in the document")
    for character in characters:
        print(f"The '{character}' character was found {characters[character]} times")
    print("--- End report ---")

main()