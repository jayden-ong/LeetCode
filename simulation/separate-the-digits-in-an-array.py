class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            string_num = str(num)
            for char in string_num:
                answer.append(int(char))
        return answer