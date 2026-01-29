class Solution:
    def trimMean(self, arr: List[int]) -> float:
        length_arr = len(arr)
        curr_sum = 0
        num_nums = 0
        arr.sort()
        for i in range(length_arr):
            if i >= int(0.05 * length_arr) and i < int(length_arr - (0.05 * length_arr)):
                curr_sum += arr[i]
                num_nums += 1
        return curr_sum / num_nums