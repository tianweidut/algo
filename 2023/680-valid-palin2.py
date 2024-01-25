class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True

        def _chk(i, j, has_removed):
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    if has_removed:
                        return False

                    return _chk(i + 1, j, True) or _chk(i, j - 1, True)

            return True

        return _chk(0, len(s) - 1, False):q
