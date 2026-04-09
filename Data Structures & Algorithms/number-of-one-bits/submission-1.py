class Solution:
    def hammingWeight(self, n: int) -> int:

        numOfOneBits = 0

        while n > 0:
            n = n & (n - 1)
            numOfOneBits += 1
        
        return numOfOneBits