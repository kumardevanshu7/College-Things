def reverse_number(number):
    reversed_number = 0

    while number > 0:
        digit = number % 10

        reversed_number = (reversed_number * 10) + digit

        number = number // 10

    return reversed_number


def calculate_average(numbers):
    if len(numbers) == 0:
        return None

    total = sum(numbers)

    average = total / len(numbers)

    return average

input_number = 12345
reversed_result = reverse_number(input_number)
print("The reverse of", input_number, "is", reversed_result)

number_list = [5, 9, 2, 11, 3, 8, 6]
average_value = calculate_average(number_list)
print("The average of the numbers is:", average_value)

print("\n\n\n Name: Kumar Devanshu \t Roll No: 2200970139009 \t Section: IT-A2")

print("\n")
