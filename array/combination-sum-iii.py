class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # The maximum sum you can make is 9 + 8 + ...
        # The highest number in any set is n - 3
        answer = []
        def choice(nums_list, curr_sum, curr_num):
            if curr_sum > n:
                return
            elif curr_sum == n:
                if len(nums_list) == k:
                    answer.append(nums_list)
                return
            
            if curr_num >= min(10, n - 2):
                return

            if len(nums_list) == k - 1:
                if n - curr_sum > curr_num and n - curr_sum <= 9:
                    copy = nums_list.copy()
                    copy.append(n - curr_sum)
                    answer.append(copy)
                    return
            
            # Can choose not to add curr_num
            choice(nums_list, curr_sum, curr_num + 1)
            # Can choose to add curr_num
            copy = nums_list.copy()
            copy.append(curr_num)
            choice(copy, curr_sum + curr_num, curr_num + 1)
            return
            
        for i in range(1, min(10, n - 2)):
            choice([i], i, i + 1)
        return answer