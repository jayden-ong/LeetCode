class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        answer = [0, 0]
        for i in range(1, 10):
            if i in nums1 and i in nums2:
                return i
            
            if i in nums1 and answer[0] == 0:
                answer[0] = i
            
            if i in nums2 and answer[1] == 0:
                answer[1] = i
            
        return min(answer) * 10 + max(answer)
