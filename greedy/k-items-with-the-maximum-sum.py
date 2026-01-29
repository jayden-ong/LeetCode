class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k
        
        answer = numOnes
        k -= numOnes
        if k <= numZeros:
            return answer
        
        k -= numZeros
        return answer - k