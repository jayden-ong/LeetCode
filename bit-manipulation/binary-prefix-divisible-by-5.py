class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        curr = ""
        num_nums = len(nums)
        answer = []
        for i in range(num_nums):
            curr += str(nums[i])
            if int(curr, 2) % 5 == 0:
                answer.append(True)
            else:
                answer.append(False)
        return answer