class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s;

        if not s:
            if not p:
                return True
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s, p[2:])
            else:
                return False

        if p[0] is not '.' and s[0] != p[0]:
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s, p[2:])
            else:
                return False

        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])

        return self.isMatch(s[1:], p[1:])

s = Solution()
print(s.isMatch("aa", "a"))
