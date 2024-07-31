class Solution(object):
    def findKthLargest(self, nums, k):
        n = len(nums)
        nums.sort()
        return nums[n-k]
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        