class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dfs(s_idx, p_idx):
            if p_idx == len(p):
                return s_idx == len(s)

            if s_idx == len(s):
                for i in range(p_idx, len(p)):
                    if p[i] != "*":
                        return False
                return True

            if (s_idx, p_idx) in memo:
                return memo[(s_idx, p_idx)]

            if p[p_idx] == s[s_idx] or p[p_idx] == "?":
                val = dfs(s_idx + 1, p_idx + 1)
            elif p[p_idx] == "*":
                val = dfs(s_idx + 1, p_idx) or dfs(s_idx + 1, p_idx + 1) or dfs(s_idx, p_idx + 1)
            else:
                val = False

            memo[(s_idx, p_idx)] = val
            return val               

        return dfs(0, 0)
        
