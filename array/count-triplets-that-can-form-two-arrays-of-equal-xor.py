class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        answer = 0
        length_arr = len(arr)
        for i in range(length_arr - 1):
            curr_res = arr[i]
            for j in range(i + 1, length_arr):
                curr_res ^= arr[j]
                if curr_res == 0:
                    answer += j - i
        return answer