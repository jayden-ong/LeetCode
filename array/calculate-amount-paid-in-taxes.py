class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        num_brackets = len(brackets)
        i = 0

        answer = 0
        while income > 0:
            if i == 0:
                amount_taxed = min(income, brackets[i][0])
                answer += amount_taxed * (brackets[i][1] / 100)
                income -= amount_taxed
            else:
                amount_taxed = min(income, (brackets[i][0] - brackets[i - 1][0]))
                answer += amount_taxed * (brackets[i][1] / 100)
                income -= amount_taxed
            i += 1
        return answer