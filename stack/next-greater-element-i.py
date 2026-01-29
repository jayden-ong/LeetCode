class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # For each element of nums1, find it in nums2 and find next greater element in nums2
        # if it exists and -1 if it doesn't
        greater_element_dict = {}
        num_nums2 = len(nums2)
        i = 0
        while i < num_nums2:
            escaped = False
            for j in range(i + 1, num_nums2):
                if nums2[i] < nums2[j]:
                    escaped = True
                    break
            
            if not escaped:
                greater_element_dict[nums2[i]] = -1
            else:
                # Want to skip traversing the list
                greater_element_dict[nums2[i]] = nums2[j]
            i += 1
        
        res = []
        for num in nums1:
            res.append(greater_element_dict[num])
        return res
        