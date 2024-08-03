class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1 = nums1 + nums2 
        nums1.sort()  
        n = len(nums1)
        
        if n % 2 == 0:
            mid1 = n // 2
            mid2 = mid1 - 1
            median = (nums1[mid1] + nums1[mid2]) / 2.0
        else:
            median = nums1[n // 2]
        
        return median
