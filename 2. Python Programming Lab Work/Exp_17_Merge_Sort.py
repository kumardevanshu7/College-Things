# Python Practical 17 : To write a python program to perform Merge Sort.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_idx = 0
    right_idx = 0
    
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    
    return merged

my_list = [23, 98, 52, 22, 111]
sorted_list = merge_sort(my_list)
print("Sorted list:", sorted_list)

print("\n\n\n Name: Kumar Devanshu \t Roll No: 2200970139009 \t Section: IT-A2")

print("\n")
