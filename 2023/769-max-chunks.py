class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        max_val = 0
        for idx in range(0, len(arr)):
            max_val = max(max_val, arr[idx])
            if max_val == idx:
                chunks += 1

        return chunks
