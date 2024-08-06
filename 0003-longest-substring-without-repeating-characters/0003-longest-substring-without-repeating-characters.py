class Solution(object):
    def lengthOfLongestSubstring(self, s):
        '''
        result = set(s)
        count = 0
        for i in result:
            count += 1
        return count
        '''
        l = 0
        count = 0
        s1 = set()
        for r in range(len(s)):
            while s[r] in s1:
                s1.remove(s[l])
                l += 1
            d = (r - l) + 1
            s1.add(s[r])
            count = max(count, d)
        return count 
            