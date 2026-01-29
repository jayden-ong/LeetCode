class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            string_num = str(num)
            highest_num = max(string_num)
            answer += int(highest_num * len(string_num))
        return answer