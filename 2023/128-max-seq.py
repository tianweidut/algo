class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_len = 0
        nums_map = {n: 1 for n in nums}

        for n in nums:
            if n not in nums_map:
                continue

            seq_max_len = 1
            queue = [n]
            while queue:
                item = queue.pop(0)

                del nums_map[item]
                if item - 1 in nums_map:
                    queue.append(item - 1)
                    seq_max_len += 1

                if item + 1 in nums_map:
                    queue.append(item + 1)
                    seq_max_len += 1

            max_len = max(max_len, seq_max_len)

        return max_len


    def longestConsecutive2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_len = 0
        nums_map = {n: 1 for n in nums}

        while nums_map:

            n = list(nums_map.keys())[0]
            seq_max_len = 1
            queue = [n]
            while queue:
                item = queue.pop(0)

                del nums_map[item]
                if item - 1 in nums_map:
                    queue.append(item - 1)
                    seq_max_len += 1

                if item + 1 in nums_map:
                    queue.append(item + 1)
                    seq_max_len += 1

            max_len = max(max_len, seq_max_len)

        return max_len

