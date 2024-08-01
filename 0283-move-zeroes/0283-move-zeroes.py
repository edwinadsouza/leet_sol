class Solution(object):
    def moveZeroes(self, nums):
        zero = []
        nonzero = []
        for num in nums:
            if num == 0:
                zero.append(num)
            else:
                nonzero.append(num)
        nums[:] = nonzero + zero
        