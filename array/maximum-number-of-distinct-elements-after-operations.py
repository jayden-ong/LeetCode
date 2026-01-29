class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = 0
        curr_count = 1
        num_alterations = 2 * k + 1
        curr_num = nums[0]
        curr_min = nums[0] - k - 1
        for i in range(1, len(nums) + 1):
            if i < len(nums) and nums[i - 1] == nums[i]:
                curr_count += 1
            else:
                # Figure out how many unique nums we can get
                smallest_alteration = curr_num - k
                # Maximum number of unique changes that can be made
                max_alterations = num_alterations - max(0, curr_min - smallest_alteration + 1)
                #print(smallest_alteration)
                #print(max_alterations)
                #print(curr_min)
                if max_alterations == num_alterations:
                    answer += min(curr_count, max_alterations)
                    curr_min = curr_num - k + min(curr_count, max_alterations) - 1
                elif max_alterations > 0:
                    answer += min(curr_count, max_alterations)
                    curr_min += min(curr_count, max_alterations)

                # Reset everything
                if i != len(nums):
                    curr_num = nums[i]
                    curr_count = 1
        return answer