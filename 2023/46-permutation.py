class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) <= 1:
            return [nums]

        results = []
        for n in nums:
            c_nums = nums.copy()
            c_nums.remove(n)

            sub_rs = self.permute(c_nums)
            for r in sub_rs:
                if r:
                    results.append([n] + r)

        return results
