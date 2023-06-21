# Python Practical 9. To write a python program to find the maximum of a list of numbers.

def find_max(nums):
    if len(nums) == 0:
        return None
    
    max = nums[0]

    for num in nums[1:]:
        if num > max:
            max = num

    return max

num_list = [5, 9, 2, 11, 3, 8, 6]
max_value = find_max(num_list)
print("The maximum value in the list is:", max_value)

print("\n\n\n Name: Kumar Devanshu \t Roll No: 2200970139009 \t Section: IT-A2")

print("\n")
