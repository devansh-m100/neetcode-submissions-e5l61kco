class Solution:
    # O(n ^ 2) time | O(n) space, where n is the length of the given input string
    def longestPalindrome(self, s: str) -> str:
        resStartIdx = 0
        resLen = 0

        def expand(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        for i in range(len(s)):
            # odd
            l1, r1 = expand(s, i, i)
            if (r1 - l1 + 1) > resLen:
                resStartIdx = l1
                resLen = r1 - l1 + 1
            
            # even
            l2, r2 = expand(s, i, i + 1)
            if (r2 - l2 + 1) > resLen:
                resStartIdx = l2
                resLen = r2 - l2 + 1

        return s[resStartIdx: resStartIdx + resLen]