class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        modulo_list = [0] * value
        for num in nums:
            modulo_list[num % value] += 1
        
        answer = float('inf')
        for i in range(len(modulo_list)):
            answer = min(answer, modulo_list[i] * value + i)
        return answer