class Solution:
    def lengthOfLongestSubstring(self, s):
        hashmap = {}
        i = 0
        j = 0
        max = 0
        while j < len(s):
            if s[j] in hashmap and hashmap[s[j]] != 0:
                hashmap[s[j]] = 2
                if j - i > max:
                    max = j - i
                while i < j:
                    if hashmap[s[i]] == 2:
                        hashmap[s[i]] = 0
                        i = i + 1
                        break
                    else:
                        hashmap[s[i]] = 0
                        i = i + 1
            hashmap[s[j]] = 1
            j = j + 1
        if j - i > max:
            max = j - i
        return max

s = Solution()
print(s.lengthOfLongestSubstring("dvdf"))