class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {}
        for num in nums1:
            if num in nums1_dict:
                nums1_dict[num] += 1
            else:
                nums1_dict[num] = 1

        nums2_dict = {}
        for num in nums2:
            if num in nums2_dict:
                nums2_dict[num] += 1
            else:
                nums2_dict[num] = 1
        
        final_list = []
        for key in nums1_dict:
            if key in nums2_dict:
                final_list += [key] * min(nums1_dict[key], nums2_dict[key])
            
        return final_list