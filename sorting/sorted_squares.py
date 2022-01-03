"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
"""

def sortArr(arr):
    for count, item in enumerate(arr):
        arr[count] = item**2
        
        
    count = 0
    previous = 0
    while count < len(arr):
        if arr[count] < previous:
            arr[count - 1] = arr[count]
            arr[count] = previous
            count = 0
        previous = arr[count]
        count+=1
    return arr


def sortArr2(arr):
    """O(n) solution"""
    output = [0] * len(arr)
    
    left_pointer = 0
    right_pointer = max_index = len(arr) - 1
    for count in range(max_index, -1, -1):
        if abs(arr[left_pointer]) > abs(arr[right_pointer]):
            output[count] = arr[left_pointer]**2
            left_pointer += 1
        else:
            output[count] = arr[right_pointer]**2
            right_pointer -= 1
    return output