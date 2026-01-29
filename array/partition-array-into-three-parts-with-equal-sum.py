class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        num_nums = len(arr)
        curr_i = 0
        arr_sum = sum(arr)
        if arr_sum % 3 != 0:
            return False
        desired_sum = arr_sum // 3
        mid_sum = arr_sum
        for i in range(1, num_nums - 1):
            curr_i += arr[i - 1]
            mid_sum -= arr[i - 1]
            if curr_i == desired_sum:
                curr_j = 0
                temp_mid_sum = mid_sum
                for j in range(num_nums - 1, i, -1):
                    curr_j += arr[j]
                    temp_mid_sum -= arr[j]
                    if curr_j == desired_sum and temp_mid_sum == desired_sum:
                        return True
        return False