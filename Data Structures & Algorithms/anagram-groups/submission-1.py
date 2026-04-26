class Solution:
    # O(m * n) time | O(m * n) space, where m is the number of strings in the list and n is the length of the longest string
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            d[tuple(count)].append(s)
        return list(d.values())