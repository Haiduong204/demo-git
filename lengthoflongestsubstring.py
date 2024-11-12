class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maxlength = 0
        # n = len(s)
        # left = 0
        # Charset = set()

        # for right in range(n):
        #     if s[right] not in Charset:
        #         Charset.add(s[right])
        #         maxlength = max(maxlength, right - left + 1)

        #     else:
        #         while s[right] in Charset:
        #             Charset.remove(s[left])
        #             left += 1
        #         Charset.add(s[right])
        # return maxlength
        lst = []
        maxsubstring = 0
        l = 0
        for r in range(len(s)):
            while s[r] in lst:
                lst.pop(0)
            lst.append(s[r])
            maxsubstring = max(maxsubstring, len(lst))
        return maxsubstring


S = Solution()
test = "abcabcbb"
print(S.lengthOfLongestSubstring(test))
