class Solution:
    def isFascinating(self, n: int) -> bool:
        concatenation = str(n) + str(n * 2) + str(n * 3)
        numbers_set = set()
        answer = 0
        for char in concatenation:
            if char not in numbers_set:
                answer += 1
                numbers_set.add(char)
            elif char in numbers_set:
                return False
            
            if char == '0':
                return False
        return answer == 9