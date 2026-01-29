class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        answer = 0
        gas_used = 0
        while mainTank > 0:
            gas_used += 1
            mainTank -= 1
            answer += 10
            if gas_used % 5 == 0 and additionalTank > 0:
                additionalTank -= 1
                mainTank += 1

        return answer