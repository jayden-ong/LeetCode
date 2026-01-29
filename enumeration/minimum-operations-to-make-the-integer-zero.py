class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # Number of operations required to convert num1 to 0 is just the number of 1 bits
        answer = 1
        while True:
            curr = num1 - num2 * answer
            if curr < answer:
                return -1
            
            if answer >= curr.bit_count():
                return answer
            answer += 1