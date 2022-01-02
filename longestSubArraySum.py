def longestSubArraySum(arr, target):
    """
    Returns the index range of the longest sub array that adds up to the target
    This solution is implemented using the sliding window approach
    at worse will run in O(2n) time
    """
    left_pointer = 0
    right_pointer = 0
    summ = 0
    output = [0, 0]

    while left_pointer < len(arr):
        if right_pointer > len(arr) - 1:
            break

        if summ <= target:
            summ += arr[right_pointer]
            right_pointer += 1
        else:
            summ -= arr[left_pointer]
            left_pointer += 1

        if (right_pointer - left_pointer) > (output[1] - output[0]) and summ == target:
            output[0] = left_pointer
            output[1] = right_pointer - 1

    return output


lst = [1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10]
index_0, index_1 = longestSubArraySum(lst, 15)
print(longestSubArraySum(lst, 15))
print([x for x in lst[index_0: index_1 + 1]])
