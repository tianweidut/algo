class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict

        loc_map = defaultdict(list)
        for f, t in tickets:
            loc_map[f].append(t)

        for k, v in loc_map.items():
            loc_map[k] = sorted(v)

        paths = []
        stack = ["JFK"]

        while stack:
            loc = stack[-1]
            
            if loc_map[loc]:
                stack.append(loc_map[loc][0])
                loc_map[loc].pop(0)
            else:
                paths.append(stack.pop(-1))

        return paths[::-1]
