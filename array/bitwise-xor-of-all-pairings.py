class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        answer = 0
        if len(nums2) % 2 == 1:
            for num in nums1:
                answer ^= num
        
        if len(nums1) % 2 == 1:
            for num in nums2:
                answer ^= num
        return answer