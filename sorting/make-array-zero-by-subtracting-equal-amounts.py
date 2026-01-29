class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0
        length_nums = len(nums)
        i = 0
        greatest_num = nums[-1]
        amount_subtracted = 0
        while greatest_num - amount_subtracted != 0:
            #print(i)
            #print(amount_subtracted)
            if nums[i] > 0 and nums[i] - amount_subtracted > 0:
                amount_subtracted += nums[i] - amount_subtracted
                answer += 1
            i += 1
        return answer