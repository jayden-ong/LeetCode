class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        required_appear = (len(arr) // 4) + 1
        curr_freq = 0
        curr_num = -1

        for num in arr:
            if curr_num == -1:
                curr_num = num
                curr_freq = 1
            elif curr_num == num:
                curr_freq += 1
                if curr_freq >= required_appear:
                    return curr_num
            else:
                curr_num = num
                curr_freq = 1
        return curr_num
            