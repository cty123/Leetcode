class Solution:
    def isP(self, int_str:str) -> bool:
        if len(int_str) == 0 or len(int_str) == 1:
            return True
        l = len(int_str)
        if int_str[0] == int_str[l-1]:
            new_str = int_str[1:l-1]
            if len(new_str) == 0:
                return True
            return self.isP(int_str[1:l-1])
        return False

    def isPalindrome(self, x: int) -> bool:
        int_str = str(x)
        return self.isP(int_str)

s = Solution()
print(s.isPalindrome(11))
