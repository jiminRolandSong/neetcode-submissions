class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    # i + j = (m + n) // 2
        m = len(nums1)
        n = len(nums2) 
        i = len(nums1) // 2
        totallen = m + n

        left = 0
        right = m

        while left <= right:
            i = (left + right) // 2
            j = (m + n) // 2 - i

            nums1_left = nums1[i-1] if i > 0 else float('-inf')
            nums1_right = nums1[i] if i < m else float('inf')
            nums2_left = nums2[j-1] if j > 0 else float('-inf')
            nums2_right = nums2[j] if j < n else float('inf')

            if nums1_left <= nums2_right and nums2_left <= nums1_right:

                leftest = max(nums1_left, nums2_left)
                rightest = min(nums1_right, nums2_right)

                if totallen % 2 == 0:
                    return (leftest + rightest) / 2
                else:
                    return rightest
            elif nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1



