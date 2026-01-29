class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_before = [-1]
        max_after = [-1]
        curr = float('-inf')
        curr2 = float('-inf')
        for i in range(1, len(nums)):
            if nums[i - 1] > curr:
                curr = nums[i - 1]
            
            max_before.append(curr)

            if nums[len(nums) - i] > curr2:
                curr2 = nums[len(nums) - i]
            
            max_after.append(curr2)
        max_after = max_after[::-1]
        print(max_before)
        print(max_after)
        answer = 0
        for i in range(1, len(nums) - 1):
            answer = max(answer, (max_before[i] - nums[i]) * max_after[i])
        return answer