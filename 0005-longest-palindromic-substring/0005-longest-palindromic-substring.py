class Solution(object):
    def longestPalindrome(self, s):
        def centre(s,l,r):
            max_len = 0
            sub = ""

            while l>= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    max_len = r - l + 1
                    sub = s[l : r + 1]
                l -= 1
                r += 1
            return sub
        result = ""
        for i in range(len(s)):
            odd = centre(s,i,i)
            even = centre(s,i,i+1)
            if len(odd)> len(result):
                result = odd
            if len(even)>len(result):
                result = even
        return result