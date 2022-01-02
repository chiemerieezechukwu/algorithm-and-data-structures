"""
Flatten any kind of nested list via recursion
"""

output = []
def flatten_list(arr):
    for val in arr:
        if isinstance(val, list):
            flatten_list(val)
        else:
            output.append(val)
    return output
            
arr = [1, [2, [3, [4, [5, [6, [7, 80, 78]]]], 8, 9]], [[10]]]
print(flatten_list(arr))