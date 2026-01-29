class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Find longest number
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        def custom_sort():
            for i in range(len(nums) - 1, 0, -1):
                for j in range(i):
                    if int(nums[j] + nums[j + 1]) < int(nums[j + 1] + nums[j]):
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
        custom_sort()
        answer = ''.join(nums)
        if answer[0] == '0':
            return '0'
        return answer
        