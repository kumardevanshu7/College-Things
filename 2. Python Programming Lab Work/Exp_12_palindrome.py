# Python Practical 12 : To write a python program to check if a number and string is a palindrome or not.

def is_palindrome(input_str):
    reversed_str = input_str[::-1]
    return input_str == reversed_str

nums = int(input("Enter a number: "))
nums_str = str(nums)
if is_palindrome(nums_str):
    print("The number", nums, "is a palindrome.")
else:
    print("The number", nums, "is not a palindrome.")

string = input("Enter a string: ")
if is_palindrome(string):
    print("The string", string, "is a palindrome.")
else:
    print("The string", string, "is not a palindrome.")

print("\n\n\n Name: Kumar Devanshu \t Roll No: 2200970139009 \t Section: IT-A2")

print("\n")
