class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
        
        ans = []
        for i in range(1, len(nums) + 1):
            if nums_dict.get(i, -1) == -1:
                ans.append(i)
        return ans