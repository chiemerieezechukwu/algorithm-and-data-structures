"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
Do not return anything, modify nums in-place instead.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""
from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    O(n*k) time
    o(1) space
    """
    k = k % len(nums)  # for k > len(nums), it is sufficient to rotate the array only by the modulo which will still be len(nums) if k < len(nums)

    for _ in range(k):
        nums.insert(0, nums.pop())

    return nums


def rotate2(nums: List[int], k: int):
    """
    Brute force
    """
    for _ in range(k):
        temp = nums[-1]
        
        for x in range(len(nums)-1, 0, -1):
            nums[x] = nums[x-1]
        
        nums[0] = temp
    
    return nums


def rotate3(nums: List[int], k: int):
    """
    Pythonic
    """
    k = k % len(nums)
    temp = nums[len(nums)-k:]
    nums[k:] = nums[:len(nums)-k]
    nums[:k] = temp

    return nums


def rotate4(nums: List[int], k: int):
    """
    Leetcode solution
    """
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            
            start += 1
            end -= 1
    
    k = k % len(nums)
    reverse(nums, 0, len(nums)-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums)-1)

    return nums

# %timeit rotate([1, 2, 3, 4, 5, 6, 7, 8], 4)
# 567 ns ± 1.78 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

# %timeit rotate2([1, 2, 3, 4, 5, 6, 7, 8], 4)
# 2.95 µs ± 1.21 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

# %timeit rotate3([1, 2, 3, 4, 5, 6, 7, 8], 4)
# 471 ns ± 0.72 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

# %timeit rotate4([1, 2, 3, 4, 5, 6, 7, 8], 4)
# 1.72 µs ± 13.3 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
