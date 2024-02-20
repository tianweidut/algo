class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict

        nmap = defaultdict(int)
        for n in nums:
            nmap[n] += 1
            if nmap[n] >= 2:
                return True

        return False
