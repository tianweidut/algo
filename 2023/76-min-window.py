class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s:
            return s

        from collections import defaultdict
        t_map = defaultdict(int)
        for x in t:
            t_map[x] += 1

        min_len, min_start = len(s) + 1, 0
        left = 0
        cnt = 0
        for right, ch in enumerate(s):
            if ch not in t_map:
                continue

            t_map[ch] -= 1
            if t_map[ch] >= 0:
                cnt += 1

            while cnt == len(t):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left 

                if s[left] in t_map:
                    t_map[s[left]] += 1
                    if t_map[s[left]] > 0:
                        cnt -= 1

                left += 1
        
        return "" if min_len > len(s) else s[min_start:min_start + min_len]
