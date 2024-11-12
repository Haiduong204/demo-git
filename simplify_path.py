class Solution(object):
    def simplifyPath(self, path):
        # create a stack contain path
        stack = []

        # Split the given path by '/' to get individual components
        path = path.split("/")

        # Iterate through each part of the split path
        for char in path:
            if char == "" or char == ".":
                continue
            elif char == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        simolify_path = "/" + "/".join(stack)
        return simolify_path if stack else "/"


S = Solution()
path = "/home//foo/"
print(S.simplifyPath(path))
