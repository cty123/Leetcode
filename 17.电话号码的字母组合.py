class Solution:
    def letterCombinations(self, digits: str):
        l = { 
            '2': list('abc'), 
            '3': list('def'), 
            '4': list('ghi'), 
            '5': list('jkl'), 
            '6': list('mno'), 
            '7': list('pqrs'), 
            '8': list('tuv'), 
            '9': list('wxyz'), 
        } 
        
        if not digits: 
            return [] 

        result = [''] 
        
        for i in digits: 
            temp = []
            for j in l[i]:
                for k in result:
                    temp.append(k + j) 
            result = temp

        return result
    
s = Solution()
print(s.letterCombinations("23"))

