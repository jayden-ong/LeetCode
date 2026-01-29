class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_length, nums2_length = len(nums1), len(nums2)
        total_length = nums1_length + nums2_length
        stop_index = total_length // 2
        is_odd = total_length % 2 == 1
        i_increase = False
        i, j = 0, 0
        if is_odd:
            for k in range(stop_index + 1):
                if i != nums1_length and (j == nums2_length or nums1[i] <= nums2[j]):
                    i += 1
                    i_increase = True
                elif j != nums2_length and (i == nums1_length or nums2[j] <= nums1[i]):
                    j += 1
                    i_increase = False
            
            if i_increase:
                return nums1[i - 1]
            return nums2[j - 1]
        else:            
            curr_val = 0
            for k in range(stop_index + 1):
                if i != nums1_length and (j == nums2_length or nums1[i] <= nums2[j]):
                    i += 1
                    i_increase = True
                elif j != nums2_length and (i == nums1_length or nums2[j] <= nums1[i]):
                    j += 1
                    i_increase = False
                
                if k == stop_index - 1 or k == stop_index:
                    if i_increase:
                        curr_val += nums1[i - 1]
                    else: 
                        curr_val += nums2[j - 1]   
            return curr_val / 2

        