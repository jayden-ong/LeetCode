class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            curr_even = curr_odd = 0
            even_dict = set()
            odd_dict = set()
            for j in range(i, len(nums)):
                if nums[j] % 2 == 0 and nums[j] not in even_dict:
                    curr_even += 1
                    even_dict.add(nums[j])
                elif nums[j] % 2 == 1 and nums[j] not in odd_dict:
                    curr_odd += 1
                    odd_dict.add(nums[j])

                if curr_even == curr_odd:
                    answer = max(answer, j - i + 1)
        return answer
            