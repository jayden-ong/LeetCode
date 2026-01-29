class Solution:
    def nearestPalindromic(self, n: str) -> str:
        poss = []
        if len(n) % 2 == 0:
            first_half = n[:len(n) // 2]
            first_half_int = int(first_half)
            poss.append(int(str(first_half) + str(first_half[::-1])))
            poss.append(int(str(first_half_int + 1) + str(first_half_int + 1)[::-1]))
            poss.append(int(str(first_half_int - 1) + str(first_half_int - 1)[::-1]))

        else: 
            first_half = n[:len(n) // 2 + 1]
            first_half_int = int(first_half)
            poss.append(int(str(first_half[:len(first_half) - 1]) + str(first_half[::-1])))
            poss.append(int(str(first_half_int + 1)[:len(first_half) - 1] + str(first_half_int + 1)[::-1]))
            poss.append(int(str(first_half_int - 1)[:len(first_half) - 1] + str(first_half_int - 1)[::-1]))
            
        poss.append(10 ** (len(n) - 1) - 1)
        poss.append(10 ** len(n) + 1)
        answer = None
        diff = float('inf')
        for num in poss:
            if num != int(n) and (abs(int(n) - num) < diff or (abs(int(n) - num) == diff and num < answer)):
                answer = num
                diff = abs(int(n) - num)
        return str(answer)