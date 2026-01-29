class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        newNums = nums
        length_new_nums = len(nums)
        while length_new_nums > 1:
            temp = newNums.copy()
            newNums = []
            length_new_nums //= 2
            for i in range(length_new_nums):
                if i % 2 == 0:
                    newNums.append(min(temp[2 * i], temp[2 * i + 1]))
                else:
                    newNums.append(max(temp[2 * i], temp[2 * i + 1]))
        return newNums[-1]