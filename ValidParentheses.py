# Valid Parantheses (easy)


def isValid(s):
    stack = []
    parenmap = {")": "(", "}": "{", "]": "["}
    for element in s:
        if len(stack) == 0 and element in parenmap:
            return False
        elif element not in parenmap:
            stack.append(element)
        elif stack.pop() != parenmap[element]:
            return False
    if len(stack) == 0:
        return True
    return False


print(isValid(")"))


# LEETCODE SOLUTIONS
# class Solution(object):
# def isValid(self, s):
#     stack = [] # create an empty stack to store opening brackets
#     for c in s: # loop through each character in the string
#         if c in '([{': # if the character is an opening bracket
#             stack.append(c) # push it onto the stack
#         else: # if the character is a closing bracket
#             if not stack or \
#                 (c == ')' and stack[-1] != '(') or \
#                 (c == '}' and stack[-1] != '{') or \
#                 (c == ']' and stack[-1] != '['):
#                 return False # the string is not valid, so return false
#             stack.pop() # otherwise, pop the opening bracket from the stack
#     return not stack # if the stack is empty, all opening brackets have been matched with their corresponding closing brackets,
#                      # so the string is valid, otherwise, there are unmatched opening brackets, so return false
