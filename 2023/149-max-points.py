class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        from collections import defaultdict
        from itertools import chain
        
        v_map = defaultdict(int)
        h_map = defaultdict(int)
        max_points = 0
        
        p_len = len(points)
        for i in range(0, p_len):
            v_map[points[i][1]] += 1
            h_map[points[i][0]] += 1

            r_map = defaultdict(int)
            for j in range(i + 1, p_len):
                if points[j][1] == points[i][1] or points[j][0] == points[i][0]:
                    continue

                ratio = (points[i][0] - points[j][0]) / (points[i][1] - points[j][1])
                r_map[ratio] += 1
            
            for v in r_map.values():
                max_points = max(max_points, v + 1)
                    
        for v in chain(v_map.values(), h_map.values()):
            max_points = max(max_points, v)
        return max_points

