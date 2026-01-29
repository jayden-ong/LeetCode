class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        prev = [[nums[0]]]
        answer = [[nums[0]]]
        num_nums = len(nums)
        for i in range(2, num_nums + 1):
            answer = []
            for sub_list in prev:
                for j in range(len(sub_list) + 1):
                    old_sublist = sub_list.copy()
                    sub_list.insert(j, nums[i - 1])
                    answer.append(sub_list)
                    sub_list = old_sublist
            prev = answer
        print(answer)
        return answer