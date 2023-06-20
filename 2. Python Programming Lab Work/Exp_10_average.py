# Python Practical 10 : To write a python program to reverse a number and also to calculate the average of number in a list.

def reverse_num(num):
    reversed_num = 0

    while num > 0:
        digit = num % 10

        reversed_num = (reversed_num * 10) + digit

        num = num // 10

    return reversed_num


def calculate_average(nums):
    if len(nums) == 0:
        return None

    total = sum(nums)

    average = total / len(nums)

    return average

input_num = 12345
reversed_result = reverse_num(input_num)
print("The reverse of", input_num, "is", reversed_result)

number_list = [5, 9, 2, 11, 3, 8, 6]
average_value = calculate_average(number_list)
print("The average of the numbers is:", average_value)

print("\n\n\n Name: Kumar Devanshu \t Roll No: 2200970139009 \t Section: IT-A2")

print("\n")
