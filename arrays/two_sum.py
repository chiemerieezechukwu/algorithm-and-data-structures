"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
"""
from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    """
    Brute force
    Time Limit Exceeded

    O(n^2) time
    O(1) space
    """
    for index, val in enumerate(numbers):
        for index2, val2 in enumerate(numbers):
            if val + val2 == target and index != index2:
                return [index+1, index2+1]


def two_sum2(numbers: List[int], target: int) -> List[int]:
    """
    O(n) time
    O(1) space
    """
    hash_table = {}
    
    for index, val in enumerate(numbers):
        complement = target - val
        if complement not in hash_table:
            hash_table[val] = index
        else:
            return [hash_table[complement]+1, index+1]


def twoSum3(numbers: List[int], target: int) -> List[int]:
    """
    The array is sorted so the operation can be done using pointers
    O(n) time
    O(1) space
    """
    start = 0
    end = len(numbers) - 1
    
    while start < end:
        sum_target = numbers[start] + numbers[end]
        if sum_target == target:
            return [start+1, end+1]
        elif sum_target < target:
            start += 1
        else:
            end -= 1