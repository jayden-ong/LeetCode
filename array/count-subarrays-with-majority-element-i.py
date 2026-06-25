class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        answer = 0
        for i in range(len(nums)):
            num_target = 0
            for j in range(i, len(nums)):
                if nums[j] == target:
                    num_target += 1
                if num_target * 2 > j - i + 1:
                    answer += 1
        return answer