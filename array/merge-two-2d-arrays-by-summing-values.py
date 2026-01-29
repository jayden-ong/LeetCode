class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums1_index = 0
        nums2_index = 0
        nums1_length = len(nums1)
        nums2_length = len(nums2)
        answer = []
        while nums1_index < nums1_length or nums2_index < nums2_length:
            if nums1_index == nums1_length:
                answer.append(nums2[nums2_index])
                nums2_index += 1
            elif nums2_index == nums2_length:
                answer.append(nums1[nums1_index])
                nums1_index += 1
            else:
                if nums1[nums1_index][0] < nums2[nums2_index][0]:
                    answer.append(nums1[nums1_index])
                    nums1_index += 1
                elif nums1[nums1_index][0] > nums2[nums2_index][0]:
                    answer.append(nums2[nums2_index])
                    nums2_index += 1
                else:
                    answer.append([nums1[nums1_index][0], nums1[nums1_index][1] + nums2[nums2_index][1]])
                    nums1_index += 1
                    nums2_index += 1
        return answer