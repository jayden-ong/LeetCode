class Solution:
    def divisorGame(self, n: int) -> bool:
        '''
        def find_factors(n):
            factors = []
            for i in range(2, int(pow(n, 0.5))):
                if n % i == 0:
                    factors.append(i)
                    factors.append(n // i)
            return factors
        answers_dict = {}
        for i in range(1, n + 1):
            if i == 1:
                answers_dict[i] = False
        '''
        return n % 2 == 0
        # 2 - alice wins - 1 
        # 3 - alice loses - 1, 1
        # 4 - alice wins - 1, 1, 1
        # 5 - alice loses - 1, 1, 1, 1
        # 6 - alice wins - 3, 1, 1
        # 7 - alice loses - 1, 3, 1, 1
        # 8 - alice wins - 1, 1, 3, 1, 1
        # 9 - alice loses 
        