class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        answer = 0
        num_empty = 0
        while numBottles > 0:
            answer += numBottles
            num_empty += (numBottles % numExchange)
            numBottles //= numExchange
            #print(num_empty)
            if num_empty // numExchange > 0:
                numBottles += (num_empty // numExchange)
                num_empty %= numExchange
        return answer