class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False

        paths = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if i in ('(', '[', '{'):
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                    
                item = stack.pop(-1)
                if item != paths[i]:
                    return False

        return len(stack) == 0
