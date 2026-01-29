class Solution:
    def sumBase(self, n: int, k: int) -> int:
        curr_amount = 0
        i = 0
        while curr_amount < n:
            curr_amount += (k - 1) * pow(k, i)
            i += 1
        
        i -= 1
        print(i)
        answer = 0
        while i >= 0:
            digit = min(k - 1, n // pow(k, i))
            answer += digit
            n -= digit * pow(k, i)
            i -= 1
        return answer