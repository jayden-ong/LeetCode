class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set()
        nums2_set = set()
        for num in nums1:
            nums1_set.add(num)
        
        second_answer = set()
        for num in nums2:
            if num not in nums1_set:
                second_answer.add(num)
            nums2_set.add(num)
        
        first_answer = set()
        for num in nums1:
            if num not in nums2_set:
                first_answer.add(num)
        
        return [list(first_answer), list(second_answer)]