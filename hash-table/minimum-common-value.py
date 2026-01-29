class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        length_nums1 = len(nums1)
        length_nums2 = len(nums2)
        nums1_index = 0
        nums2_index = 0
        while nums1_index < length_nums1 or nums2_index < length_nums2:
            if nums1[nums1_index] == nums2[nums2_index]:
                return nums1[nums1_index]
            elif nums1[nums1_index] < nums2[nums2_index]:
                if nums1_index == length_nums1 - 1:
                    return -1
                nums1_index += 1
            else:
                if nums2_index == length_nums2 - 1:
                    return -1
                nums2_index += 1
        return -1
