# Python Practical 16 : To write a python program to perform Insertion Sort.

def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr

my_list = [64, 25, 12, 22, 11]
sorted_list = insertion_sort(my_list)
print("Sorted List:", sorted_list)

print("\n\n\n Name: Kumar Devanshu \t Roll No: 2200970139009 \t Section: IT-A2")

print("\n")
