def isValid(self, s: str) -> bool:
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for i in s:
        if i in "(,[,{":
            stack.append(i)
        else:
            if not stack or (c == ")" and stack[-1] == "(")(
                c == "]" and stack[-1] == "["
            )(c == "}" and stack[-1] == "{"):
                return False
        stack.pop()
    return not stack


s = "(]"

print(isValid(None, s))
