class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        cnt = 0
        prev = intervals[0][1]
        idx = 1
        while idx < len(intervals):
            if intervals[idx][0] < prev:
                cnt += 1
            else:
                prev = intervals[idx][1]
            idx += 1

        return cnt
