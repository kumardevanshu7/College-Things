# Python Practical 08. To write a python program that counts the number of times the word "name" occurs in a string.

def count_word(string, word):
    count = 0
    words = string.split()

    for w in words:
        cleaned_word = w.strip(".,!?")

        if cleaned_word.lower() == word.lower():
            count += 1

    return count

input = "My name is Dev. What is your name? My name is not Tushpendra."
target_word = "name"
occurrences = count_word(input, target_word)
print("Word '{}' occurs {} times.".format(target_word, occurrences))

print("\n\n\n Name: Kumar Devanshu \t Roll No: 2200970139009 \t Section: IT-A2")

print("\n")
