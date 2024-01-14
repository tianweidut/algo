class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(s_idx, p_idx):
            if p_idx == len(p):
                return s_idx == len(s)

            if s_idx == len(s):
                if (len(p) - p_idx) % 2 != 0:
                    return False

                for i in range(p_idx + 1, len(p), 2):
                    if p[i] != "*":
                        return False

                return True

            key = (s_idx, p_idx) 
            if key in memo:
                return memo[key]   

            ret = False
            if s[s_idx] == p[p_idx] or p[p_idx] == ".":
                # match
                if p_idx + 1 < len(p) and p[p_idx + 1] == "*":
                    # *-zero, *-many
                    ret = dp(s_idx, p_idx + 2) or dp(s_idx + 1, p_idx)
                else: 
                    ret = dp(s_idx + 1, p_idx + 1)
            else:
                # mismatch
                if p_idx + 1 < len(p) and p[p_idx + 1] == "*":
                    ret = dp(s_idx, p_idx + 2)
                else:
                    ret = False 
            memo[key] = ret
            return ret

        return dp(0, 0)
