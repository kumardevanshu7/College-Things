def count_word_occurrences(string, word):
    count = 0
    words = string.split()

    for w in words:
        cleaned_word = w.strip(".,!?")

        if cleaned_word.lower() == word.lower():
            count += 1

    return count

input_string = "My name is Dev. What is your name? My name is not Tushpendra."
target_word = "name"
occurrences = count_word_occurrences(input_string, target_word)
print("Word '{}' occurs {} times.".format(target_word, occurrences))

print("\n\n\n Name: Kumar Devanshu \t Roll No: 2200970139009 \t Section: IT-A2")

print("\n")
