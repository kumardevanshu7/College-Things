# Python Practical 05 - To write a python program to count the number of Vowels in a string.

def count_vowels(string):
    vowels = "aeiouAEIOU"
    v_count = 0

    for char in string:
        if char in vowels:
            v_count += 1

    return v_count


# taking input from user
word = input("Enter a string: ")

no_vowels = count_vowels(word)

print("Number of vowels are:", no_vowels)

print("\n\n\n Name: Kumar Devanshu \t Roll No: 2200970139009 \t Section: IT-A2")

print("\n")
