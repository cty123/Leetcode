import numpy as np

class Solution:
    def longestPalindrome(self, s):
        max = 0
        substr = ''
        arr = np.zeros((len(s),len(s)))
        for i in range(len(s)):
            arr[i][i] = 1
            if max != 1:
                    max = 1
                    substr = s[i]
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                arr[i][i+1] = 1
                if max != 2:
                    max = 2
                    substr = s[i:i+2]
        for j in range(2, len(s)):
            for i in range(0, len(s) - j): 
                if arr[i+1][i+j-1] == 1 and s[i] == s[i+j]:
                    arr[i][j+i] = 1
                    leng = j + i - i + 1
                    if leng > max:
                        max = leng
                        substr = s[i:j+i+1]
        return substr
s = Solution()
print(s.longestPalindrome("abbc"))