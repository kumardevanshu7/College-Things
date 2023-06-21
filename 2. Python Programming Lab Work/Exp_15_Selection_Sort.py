# Python Practical 15 : To write a python program to perform Selection Sort.

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

my_list = [64, 25, 12, 22, 11]
sorted_list = selection_sort(my_list)
print("Sorted ist:", sorted_list)

print("\n\n\n Name: Kumar Devanshu \t Roll No: 2200970139009 \t Section: IT-A2")

print("\n")
