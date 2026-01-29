class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = {}
        answer = float('-inf')
        def find_max(index1, index2):
            if index1 >= len(nums1) or index2 >= len(nums2):
                return float('-inf')
            
            if (index1, index2) in dp:
                return dp[(index1, index2)]
            
            curr_product = nums1[index1] * nums2[index2]
            answer = max([curr_product, curr_product + find_max(index1 + 1, index2 + 1), find_max(index1 + 1, index2), find_max(index1, index2 + 1)])
            dp[(index1, index2)] = answer
            return answer
        
        return find_max(0, 0)
