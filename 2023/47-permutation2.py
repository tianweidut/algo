class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        

        def dfs(start):
            if start == len(nums) - 1:
                print(nums.copy())
                results.append(nums.copy())
                return

            handled_map = {}
            for idx in range(start, len(nums)):
                if nums[idx] in handled_map:
                    continue
                    
                handled_map[nums[idx]] = True

                nums[idx], nums[start] = nums[start], nums[idx]
                dfs(start + 1)
                nums[idx], nums[start] = nums[start], nums[idx]

        results = []
        dfs(0)
        return results
        
