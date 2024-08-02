class Solution(object):
    def productExceptSelf(self, nums):
        left_mul = 1
        right_mul = 1
        n = len(nums)
        left = [0] * n
        right = [0] * n

        for i in range(n):
            j = -i - 1
            left[i] = left_mul
            right[j] = right_mul
            left_mul *=nums[i]
            right_mul *=nums[j]
        return[l*r for l,r in zip(left,right)]



        