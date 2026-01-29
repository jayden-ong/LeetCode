class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        most_candies = max(candies)
        answer = []
        for kid_candy in candies:
            if kid_candy + extraCandies >= most_candies:
                answer.append(True)
            else:
                answer.append(False)
        return answer