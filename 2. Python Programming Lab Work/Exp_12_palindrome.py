def is_palindrome(input_str):
    reversed_str = input_str[::-1]
    return input_str == reversed_str

number = int(input("Enter a number: "))
number_str = str(number)
if is_palindrome(number_str):
    print("The number", number, "is a palindrome.")
else:
    print("The number", number, "is not a palindrome.")

string = input("Enter a string: ")
if is_palindrome(string):
    print("The string", string, "is a palindrome.")
else:
    print("The string", string, "is not a palindrome.")

print("\n\n\n Name: Kumar Devanshu \t Roll No: 2200970139009 \t Section: IT-A2")

print("\n")
