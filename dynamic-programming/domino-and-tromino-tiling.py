class Solution:
    def numTilings(self, n: int) -> int:
        MOD = pow(10, 9) + 7
        answers_dict = {}
        def recursive(n):
            if n in answers_dict:
                return answers_dict[n]
            
            if n == 1:
                return 1
            elif n == 2:
                return 2
            elif n == 3:
                return 5
            answer = recursive(n - 1) * 2 + recursive(n - 3)
            answers_dict[n] = answer
            return answer

        return recursive(n) % MOD