class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n != 0:
            curr_index = m + n - 1
            nums1_index = m - 1
            nums2_index = n - 1
            while nums1_index >= 0 or nums2_index >= 0:
                if nums1_index < 0:
                    nums1[curr_index] = nums2[nums2_index]
                    nums2_index -= 1
                elif nums2_index < 0:
                    nums1[curr_index] = nums1[nums1_index]
                    nums1_index -= 1
                elif nums1[nums1_index] >= nums2[nums2_index]:
                    nums1[curr_index] = nums1[nums1_index]
                    nums1_index -= 1
                elif nums1[nums1_index] < nums2[nums2_index]:
                    nums1[curr_index] = nums2[nums2_index]
                    nums2_index -= 1
                curr_index -= 1

        