class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # [1,1,1] - 5
        answer = 0
        while amount[0] != 0 or amount[1] != 0 or amount[2] != 0:
            if amount[0] != 0 and amount[1] == 0 and amount[2] == 0:
                return answer + amount[0]
            elif amount[0] == 0 and amount[1] != 0 and amount[2] == 0:
                return answer + amount[1]
            elif amount[0] == 0 and amount[1] == 0 and amount[2] != 0:
                return answer + amount[2]
            
            least_water = min(amount)
            index_least = amount.index(least_water)

            if index_least == 0:
                amount[1] -= 1
                amount[2] -= 1
            elif index_least == 1:
                amount[0] -= 1
                amount[2] -= 1
            elif index_least == 2:
                amount[0] -= 1
                amount[1] -= 1
            
            answer += 1
        return answer