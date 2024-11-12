class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1

        for index, char in enumerate(s):
            if count[char] == 1:
                return index

        return -1


S = Solution()
s = "loveleetcode"
print(S.firstUniqChar(s))
