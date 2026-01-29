class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length_nums = len(nums)
        # The default is everything is negative
        left = length_nums - 1
        right = length_nums
        for i in range(length_nums):
            if nums[i] == 0:
                left = i - 1
                right = i
                break
            else:
                if i > 0:
                    if nums[i - 1] < 0 and nums[i] > 0:
                        left = i - 1
                        right = i
                        break
                        # There is no 0, since non-decreasing
                    elif nums[i] > 0:
                        right = 0
                        left = -1
                        break

        answer = []
        while left > -1 or right < length_nums:
            if left == -1:
                answer.append(nums[right] * nums[right])
                right += 1
            elif right == length_nums:
                answer.append(nums[left] * nums[left])
                left -= 1
            else:
                if nums[right] * nums[right] < nums[left] * nums[left]:
                    answer.append(nums[right] * nums[right])
                    right += 1
                else:
                    answer.append(nums[left] * nums[left])
                    left -= 1
        return answer