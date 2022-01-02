"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List


def linear_search(nums: List[int], target: int) -> int:
    """
    O(n) solution
    """
    for index, val in enumerate(nums):
        if val == target:
            return index
    return -1


def binary_search(nums: List[int], target: int) -> int:
    """
    O(log n) solution
    """
    start = 0
    end = len(nums) - 1

    while end >= start:
        mid = (start + end) // 2
        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            return mid

    return -1
