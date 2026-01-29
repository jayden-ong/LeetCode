class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # 1 2 3 4 -> 
        # 5 6 7 8
        # 6 8 10 12
        answer = [0] * num_people
        i = 0
        while candies > 0:
            answer[i % num_people] += min(i + 1, candies)
            candies -= min(i + 1, candies)
            i += 1
        return answer