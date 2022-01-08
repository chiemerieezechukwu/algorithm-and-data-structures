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

def moveZeroes2(nums: List[int]):
    """
    Do not return anything, modify nums in-place instead.

    O(n) time
    O(1) space
    """
    next_non_zero_index = 0  # the position where the next non-zero element will go
    found_zero_count = 0
    
    # keep track of the last non-zero and when the next non-zer0 comes, append just after the last non-zero
    for index in range(len(nums)):
        if nums[index] != 0:
            nums[next_non_zero_index] = nums[index]
            next_non_zero_index += 1
        else:
            found_zero_count += 1
    
    for index in range(next_non_zero_index, len(nums)):
        nums[index] = 0

    return nums


def moveZeroes3(nums: List[int]):
    """
    Do not return anything, modify nums in-place instead.

    O(n) time
    O(1) space
    """
    
    next_non_zero_index = 0  # the position where the next non-zero element will go
    
    for index in range(len(nums)):
        if nums[index] != 0:
            nums[next_non_zero_index], nums[index] = nums[index], nums[next_non_zero_index]
            next_non_zero_index += 1

    return nums


# %timeit moveZeroes([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
# 1.69 µs ± 4.78 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

# %timeit moveZeroes2([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
# 1.25 µs ± 5.1 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

# %timeit moveZeroes3([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
# 663 ns ± 3.62 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

"""
For the set of iterations below, there isn't an outright performance benefit for `moveZeroes3(nums)`
because of the nature of the array. `moveZeroes3(nums)` is a nice optimization as it will deliver up to 250% faster
performance if the list has very few non-zero elements
"""

# %timeit moveZeroes([0,0,1,0,3,12,0,9,7,3,6,9,2,6,0,0,2])
# 1.58 µs ± 6.17 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

# %timeit moveZeroes2([0,0,1,0,3,12,0,9,7,3,6,9,2,6,0,0,2])
# 1.32 µs ± 5.56 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

# %timeit moveZeroes3([0,0,1,0,3,12,0,9,7,3,6,9,2,6,0,0,2])
# 1.23 µs ± 6.82 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)