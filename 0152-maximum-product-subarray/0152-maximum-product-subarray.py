class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0
        
        max_current = min_current = max_global = nums[0]
        
        for num in nums[1:]:
            if num < 0:
                max_current, min_current = min_current, max_current
            
            max_current = max(num, max_current * num)
            min_current = min(num, min_current * num)
            
            if max_current > max_global:
                max_global = max_current
        
        return max_global

        