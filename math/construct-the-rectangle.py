class Solution:
    def constructRectangle(self, area: int) -> List[int]:        
        def find_factors(num):
            i = 1
            res = []
            while i <= pow(num, 1/2):
                if num % i == 0:
                    res.append([num // i, i])
                i += 1
            return res
        
        return find_factors(area)[-1]