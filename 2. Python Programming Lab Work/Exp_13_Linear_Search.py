def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  

numbers = [5, 9, 2, 11, 3, 8, 6]
target_value = 3
index = linear_search(numbers, target_value)

if index != -1:
    print("The target value", target_value, "is found at index", index)
else:
    print("The target value", target_value, "is not found in the list.")

print("\n\n\n Name: Kumar Devanshu \t Roll No: 2200970139009 \t Section: IT-A2")

print("\n")
