class Solution(object):
    def nextPermutation(self, nums):
        length = len(nums)
        if length <=2:
            return nums.reverse()
        point = length - 2

        while point >=0 and nums[point] >= nums[point+1]:
            point-=1
        if point == -1:
            return nums.reverse()
        
        for i in range(length - 1, point,-1):
            if nums[point] < nums[i]:
                nums[point], nums[i] = nums[i], nums[point]
                break
        nums[point+1:] = reversed(nums[point+1:])
        