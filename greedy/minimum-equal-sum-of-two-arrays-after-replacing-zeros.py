class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_zero = 0
        nums1_sum = 0
        nums2_zero = 0
        nums2_sum = 0
        for num in nums1:
            nums1_sum += num
            if num == 0:
                nums1_zero += 1
        
        for num in nums2:
            nums2_sum += num
            if num == 0:
                nums2_zero += 1
        
        if (nums1_zero == 0 and nums1_sum < nums2_sum + nums2_zero) or (nums2_zero == 0 and nums2_sum < nums1_sum + nums1_zero):
            return -1
        
        return max(nums1_sum + nums1_zero, nums2_sum + nums2_zero)