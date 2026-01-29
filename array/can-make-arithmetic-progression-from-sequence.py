class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        num_nums = len(arr)
        curr_diff = arr[1] - arr[0]
        for i in range(2, num_nums):
            if arr[i] - arr[i - 1] != curr_diff:
                return False
        return True