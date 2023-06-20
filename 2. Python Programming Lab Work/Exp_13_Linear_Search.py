# Python Practical 13 : To write a python program to perform Linear Search.

def linear_search(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i  
    return -1  

nums = [5, 9, 2, 11, 3, 8, 6]
item = 3
idx = linear_search(nums, item)

if idx != -1:
    print("The item", item, "is found at index.", idx)
else:
    print("The item", item, "is not found in the list.")

print("\n\n\n Name: Kumar Devanshu \t Roll No: 2200970139009 \t Section: IT-A2")

print("\n")
