class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for num in range(n + 1):
            output.append(self.numberOfOnes(num))
        return output
    
    def numberOfOnes(self, num):
        count = 0
        while num:
            num &= num - 1
            count += 1
        return count