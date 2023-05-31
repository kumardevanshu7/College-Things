# Python Practical 06 - To write a python program to find the most frequent words in a text file.

from collections import Counter

def most_frequent_words(file):
    with open(file, 'r') as file:
        text = file.read()

    words = text.lower().split()

    word_counts = Counter(words)

    most_frequent = word_counts.most_common(5)

    print("The most frequent words are: ")

    for word, count in most_frequent: print(f"{word}:{count}")


filename = 'Exp_06_words.txt'

most_frequent_words(filename)

print("\n\n\n Name: Kumar Devanshu \t Roll No: 2200970139009 \t Section: IT-A2")

print("\n")