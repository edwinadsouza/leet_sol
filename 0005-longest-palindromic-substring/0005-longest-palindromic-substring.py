class Solution(object):
    def longestPalindrome(self, s):
        def center(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]  
        result = ""
        for i in range(len(s)): 
            odd = center(s, i, i)            
            even = center(s, i, i + 1)           
            result = max(result, odd, even, key=len)        
        return result
