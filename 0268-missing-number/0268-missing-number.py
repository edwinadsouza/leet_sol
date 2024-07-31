class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        nums = sorted(nums)
        sum = 0
        for i in range(n+1):
            sum+=i
            if i in nums:
                sum-=i
        return sum


        """
        :type nums: List[int]
        :rtype: int
        """
        