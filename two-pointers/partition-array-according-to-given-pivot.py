class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before = []
        between = []
        after = []
        for num in nums:
            if num < pivot:
                before.append(num)
            elif num == pivot:
                between.append(num)
            else:
                after.append(num)
        
        return before + between + after