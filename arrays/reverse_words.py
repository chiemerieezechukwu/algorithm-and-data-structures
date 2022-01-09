"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""


def reverseWords(s: str) -> str:
    """
    Pythonic
    """
    # Can be broken down in 4 steps
    # 1. Reverse the string
    # 2. Split into an array using " "
    # 3. Reverse the array
    # 4. Join to a string by " "

    #          4       1        2       3
    return " ".join(s[::-1].split(" ")[::-1])


def reverseWords2(s: str) -> str:
    temp_list = s.split(" ")
    
    start = 0
    end = len(temp_list) - 1

    # reverse the array
    while start < end:
        temp_list[start], temp_list[end] = temp_list[end], temp_list[start]
        start += 1
        end -= 1
        
    temp_str = " ".join(temp_list)
    ret = ""
    # append to a new string variable from the end
    for i in range(len(temp_str)-1, -1, -1):
        ret += temp_str[i]
        
    return ret