class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Assume 1 means there is a flower already planted
        num_flowerbeds = len(flowerbed)
        passed_one = False
        for i in range(num_flowerbeds):
            if flowerbed[i] == 0:
                if i == 0:
                    # Want to check flower to the right
                    if num_flowerbeds == 1:
                        n -= 1
                        flowerbed[i] = 1
                    else:
                        if flowerbed[i + 1] == 0:
                            n -= 1
                            flowerbed[i] = 1
                elif i == num_flowerbeds - 1:
                    # We know there must be at least two flowerbeds
                    if flowerbed[i - 1] == 0:
                        n -= 1
                        flowerbed[i] = 1
                else:
                    # We know there must be at least three flowerbeds
                    if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n -= 1

        return n <= 0