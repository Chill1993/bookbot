import os

def read_text(file):
    with open(file) as f:
        text = f.read()
    return text

def word_counter(text):
    return len(text.split( ))

def character_counter(text):
    counter_dict = {}

    for char in text:
        if char.isalpha():
            char = char.lower()

            if char in counter_dict:
                counter_dict[char] += 1
            else:
                counter_dict[char] = 1

    return counter_dict

def book_report(file):
    filename = os.path.basename(file)
    text = read_text(file)
    words = word_counter(text)
    letter_counts = character_counter(text)
    counts_list = list(letter_counts.items())
    counts_sorted = sorted(counts_list, key=lambda x: x[0])
    print(f"--- Begin report of {filename} ---")
    print(f"{words} words found in the document")
    print("\n")
    for count in counts_sorted:
        print(f"the '{count[0]}' character waas found {count[1]} times")
    print("--- End report ---")


file = './books/frankenstein.txt'
text = read_text(file)

words = word_counter(text)
letter_counts = character_counter(text)
book_report(file)
# print(words)