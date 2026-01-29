class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        num_nums = len(nums)
        answer_dict = {}
        for i in range(num_nums - 1):
            if nums[i] == key:
                if nums[i + 1] in answer_dict:
                    answer_dict[nums[i + 1]] += 1
                else:
                    answer_dict[nums[i + 1]] = 1
        
        answer = None
        curr_max = 0
        for num in answer_dict:
            if answer_dict[num] > curr_max:
                answer = num
                curr_max = answer_dict[num]
        return answer