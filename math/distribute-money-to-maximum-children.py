class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        money -= children
        # Represents how many children can have 8 dollars
        answer = min(money // 7, children)
        money -= answer * 7
        # 3 dollars remaining, so one person gets less money 
        if (money == 3 and answer > 0 and answer == children - 1) or (answer == children and money > 0):
            return answer - 1
        return answer