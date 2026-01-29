class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        length_arr = len(arr)
        curr_min_diff = arr[1] - arr[0]
        curr_answer = [[arr[0], arr[1]]]
        for i in range(2, length_arr):
            if arr[i] - arr[i - 1] < curr_min_diff:
                curr_answer = [[arr[i - 1], arr[i]]]
                curr_min_diff = arr[i] - arr[i - 1]
            elif arr[i] - arr[i - 1] == curr_min_diff:
                curr_answer.append([arr[i - 1], arr[i]])
        return curr_answer