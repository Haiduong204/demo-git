""""
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring
"""


class Solution(object):
    def longestValidParentheses(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """

        stack = [-1]  # initialize the stack with -1 to handle this base case
        max_length = 0  # create a valiable to keep track maximum of valid parentheses(valid parentheses: dau ngoac don hop le)
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:  # If the character is a closing parenthesis
                stack.pop()
                if not stack:
                    stack.append(i)
                else:

                    max_length = max(max_length, i - stack[-1])
        return max_length


S = Solution()
print(S.longestValidParentheses("(())"))

# suppose: S = "(()"
"""
b1: loop for-> fisrt element "(": --> i = 0p
    push id 0 in stack: -> stack = [-1, 0]
b2: loop for -> sencond element: "(" --> i = 1
    pusd id 1 in stack: -> stack = [-1 , 0, 1]
b2: loop for -> three element: ')' : --> i = 2
    remove "1" from stack: ->> stack = [-1,0]
    calculater max_length valid perantheses:
    valid length: max_length, i - stack[-1] = 2 - 0= 2
    return 2
    break
"""
