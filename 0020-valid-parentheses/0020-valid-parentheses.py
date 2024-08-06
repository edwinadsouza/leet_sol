class Solution(object):
    def isValid(self, s):
        d = {')':'(',']':'[','}':'{'}
        stack = []
        for c in s:
            if c not in d:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    pop = stack.pop()
                    if pop != d[c]:
                        return False
        return not stack
        