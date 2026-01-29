class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        num_nums = len(nums)
        nums.sort()
        answer = float('inf')
        if k == 1:
            return 0

        #print(nums)
        for i in range(k, num_nums + 1):
            temp = nums[i - k:i]
            #print(temp)
            answer = min(answer, temp[-1] - temp[0])
            #print(answer)
        
        return answer