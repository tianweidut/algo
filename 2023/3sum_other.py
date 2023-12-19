class Solution:
    def threeSum(self, nums):
        from collections import defaultdict

        store = defaultdict(int)
        for n in nums:
            store[n] += 1

        results = set()
        for n, c in store.items():
            new_store = store.copy()
            if c == 1:
                new_store.pop(n)
            else:
                new_store[n] -= 1

            for rs in self.twoSum(0 - n, new_store):
                results.add(tuple(sorted([n] + rs)))

        return list(map(list, results))

    def twoSum(self, target, store):
        results = []
        for n, c in store.items():
            remain = target - n
            if remain not in store:
                continue

            if remain == n:
                if c == 1:
                    continue
                else:
                    results.append([n, n])
            else:
                results.append([n, remain])

        return results



if __name__ == "__main__":
    print(Solution().threeSum([0, 0, 0]))
    print(Solution().threeSum([-1,0,1,2,-1,-4]))
