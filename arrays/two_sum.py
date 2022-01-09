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
    hash_table = {}
    
    for index, val in enumerate(numbers):
        complement = target - val
        if complement not in hash_table:
            hash_table[val] = index
        else:
            return [hash_table[complement]+1, index+1]