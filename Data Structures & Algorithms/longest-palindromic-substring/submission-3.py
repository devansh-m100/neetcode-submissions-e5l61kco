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

        def updatePalindrome(l, r, resStartIdx, resLen):
            if (r - l + 1) > resLen:
                return l, r - l + 1
            return resStartIdx, resLen

        for i in range(len(s)):
            # odd
            l1, r1 = expand(s, i, i)
            resStartIdx, resLen = updatePalindrome(l1, r1, resStartIdx, resLen)
            
            # even
            l2, r2 = expand(s, i, i + 1)
            resStartIdx, resLen = updatePalindrome(l2, r2, resStartIdx, resLen)

        return s[resStartIdx: resStartIdx + resLen]