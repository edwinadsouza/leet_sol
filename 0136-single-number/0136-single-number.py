class Solution(object):
    def singleNumber(self, nums):
        ans = 0
        for val in nums:
            ans = ans ^ val
        return ans
        """
        :type nums: List[int]
        :rtype: int
        """
        