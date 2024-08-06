class Solution(object):
    def isPalindrome(self, s):
        s1 = ''.join(char.lower() for char in s if char.isalnum())
        return s1 == s1[::-1]

        