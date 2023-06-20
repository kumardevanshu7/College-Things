# Python Practical 14 : To write a python program to perform Binary Search.

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == item:
            return mid 
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1

    return -1 

numbers = [2, 3, 5, 6, 8, 9, 11]
item = 8
idx = binary_search(numbers, item)

if idx != -1:
    print("The item", item, "is found at index.", idx)
else:
    print("The item", item, "is not found in the list.")

print("\n\n\n Name: Kumar Devanshu \t Roll No: 2200970139009 \t Section: IT-A2")

print("\n")
