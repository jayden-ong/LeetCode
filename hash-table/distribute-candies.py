class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        """
        candy_dict = {}
        num_variety = 0
        num_candy = 0
        for candy in candyType:
            if candy in candy_dict:
                candy_dict[candy] += 1
            else:
                candy_dict[candy] = 1
                num_variety += 1
            num_candy += 1
        return min(num_candy // 2, num_variety)
        """

        return min(len(candyType) // 2, len(set(candyType)))