class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums_dict = {}
        answer = 0
        for num in nums:
            if num in nums_dict:
                if nums_dict[num] == 1:
                    answer -= num
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
                answer += num
        return answer
                