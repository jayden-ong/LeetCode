class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        num_nums = len(nums)
        prev = nums[0]
        answer = 0
        hill = None
        for i in range(1, num_nums - 1):
            if nums[i] != prev:
                if nums[i] > prev:
                    hill = True
                else:
                    hill = False
                
                if nums[i] > nums[i + 1] and hill:
                    answer += 1
                    hill = False
                    prev = nums[i]
                elif nums[i] < nums[i + 1] and not hill:
                    answer += 1
                    hill = True
                    prev = nums[i]
                
        return answer
