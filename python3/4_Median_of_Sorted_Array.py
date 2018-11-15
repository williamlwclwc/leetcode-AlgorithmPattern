import sys

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        # if m+n is odd, then m+n+1//2 == m+n+2//2
        left = (m + n + 1) // 2
        right = (m + n + 2) // 2
        return (self.findkth(nums1, 0, nums2, 0, left) + 
                self.findkth(nums1, 0, nums2, 0, right)) / 2
    
    # find kth number from two sorted array
    # i, j for the starting point of nums1 & nums2
    def findkth(self, nums1, i, nums2, j, k):
        # corner cases
        if i >= len(nums1):
            # nums1 is null, find kth number of nums2
            return nums2[j + k - 1]
        if j >= len(nums2):
            # nums2 is null, find kth number of nums1
            return nums1[i + k - 1]
        if k == 1:
            # if find the first number, compare the starting number
            return min(nums1[i], nums2[j])
        # check if k/2 number exist in nums1
        if i + k // 2 - 1 < len(nums1):
            midv1 = nums1[i + k // 2 - 1]
        else:
            midv1 = sys.maxsize
        # check if k/2 number exist in nums2
        if j + k // 2 - 1 < len(nums2):
            midv2 = nums2[j + k // 2 - 1]
        else:
            midv2 = sys.maxsize
        # compare mid values of nums1&2, eliminate the smaller one's first half
        if midv1 < midv2:
            # remove k/2 numbers of nums1
            return self.findkth(nums1, i + k // 2, nums2, j, k - k // 2)
        else:
            # remove k/2 numbers of nums2
            return self.findkth(nums1, i, nums2, j + k // 2, k - k // 2)
                 
                 