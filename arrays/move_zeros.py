"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
"""
from typing import List

def moveZeroes(nums: List[int]):
    """
    Do not return anything, modify nums in-place instead.

    O(n) time
    O(n) space
    """
    res = []
    
    found_zero_count = 0

    # find the number of zero occurences and populate the new list
    for val in nums:
        if val == 0:
            found_zero_count += 1
        else:
            res.append(val)
    
    # append zeros to the new list
    for _ in range(found_zero_count):
        res.append(0)
    
    # assign the values in the new list to the original list
    for index, num in enumerate(res):
        nums[index] = num

    return nums