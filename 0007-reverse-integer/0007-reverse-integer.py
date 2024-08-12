class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        is_negative = x < 0
        x = abs(x)
        
        while x > 0:
            a = x % 10
            if rev > (2**31 - 1 - a) // 10:
                return 0
            rev = rev * 10 + a
            x = x // 10
        
        if is_negative:
            rev = -rev
        
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        
        return rev
