class Solution(object):
    def trap(self, height):
        n = len(height)
        if n < 1:
            return 0
        ans = 0
        left = [0]*n
        right = [0]*n

        left[0] = height[0]
        for i in range(1,n):
            left[i] = max(left[i-1], height[i])

        right[-1] = height[-1]
        for i in range(n-2,-1,-1):
            right[i] = max(right[i+1],height[i])

        for i in range(n):
            ans+= min(left[i],right[i]) - height[i]
        return ans

        