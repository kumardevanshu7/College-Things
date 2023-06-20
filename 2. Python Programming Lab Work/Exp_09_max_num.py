def find_maximum(numbers):
    if len(numbers) == 0:
        return None
    
    maximum = numbers[0]

    for num in numbers[1:]:
        if num > maximum:
            maximum = num

    return maximum

number_list = [5, 9, 2, 11, 3, 8, 6]
maximum_value = find_maximum(number_list)
print("The maximum value in the list is:", maximum_value)

print("\n\n\n Name: Kumar Devanshu \t Roll No: 2200970139009 \t Section: IT-A2")

print("\n")
