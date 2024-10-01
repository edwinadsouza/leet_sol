class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        # k is the position of the last unique element's index
        k = 1  # Start at 1 because the first element is always unique
        
        for i in range(1, len(nums)):  # Start from the second element
            if nums[i] != nums[i - 1]:  # Check if it's a new unique element
                nums[k] = nums[i]  # Place it at the kth position
                k += 1  # Move k forward to store the next unique element
        
        return k  # The length of the array with unique elements
