class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1   # final valid indices

        for i in range(len(s)):
            # odd length
            l1, r1 = expand(i, i)
            if (r1 - l1 + 1) > resLen:
                resIdx, resLen = l1, r1 - l1 + 1

            # even length
            l2, r2 = expand(i, i + 1)
            if (r2 - l2 + 1) > resLen:
                resIdx, resLen = l2, r2 - l2 + 1

        return s[resIdx: resIdx + resLen]