class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        cnt = 0
        smap = defaultdict(int)
        smap[0] = 1
        sval = 0
        for n in nums:
            sval += n
            cnt += smap.get(sval - k, 0)
            smap[sval] += 1

        return cnt

