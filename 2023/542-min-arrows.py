class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        cnt = 0
        prev = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] <= prev:
                cnt += 1
            else:
                prev = points[i][1]

        return len(points) - cnt
