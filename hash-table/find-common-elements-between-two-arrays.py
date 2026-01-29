class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {}
        nums2_dict = {}
        for num in nums1:
            if num not in nums1_dict:
                nums1_dict[num] = 1
            else:
                nums1_dict[num] += 1
        
        for num in nums2:
            if num not in nums2_dict:
                nums2_dict[num] = 1
            else:
                nums2_dict[num] += 1
        
        answer1 = 0
        answer2 = 0
        for num in nums1_dict:
            if num in nums2_dict:
                answer1 += nums1_dict[num]
        
        for num in nums2_dict:
            if num in nums1_dict:
                answer2 += nums2_dict[num]
        return [answer1, answer2]