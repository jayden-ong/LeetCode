class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        final_set = set()
        for item in set1:
            if item in set2:
                final_set.add(item)
        return list(final_set)