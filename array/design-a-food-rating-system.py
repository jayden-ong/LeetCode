class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.highest_ratings = defaultdict(list)
        self.foods = {}
        for i in range(len(foods)):
            heapq.heappush(self.highest_ratings[cuisines[i]], (-ratings[i], foods[i]))
            self.foods[foods[i]] = (cuisines[i], ratings[i])
        
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.foods[food]
        heapq.heappush(self.highest_ratings[cuisine], (-newRating, food))
        self.foods[food] = (cuisine, newRating)

    def highestRated(self, cuisine: str) -> str:
        curr_rating, curr_food = self.highest_ratings[cuisine][0]
        while self.highest_ratings[cuisine] and -curr_rating != self.foods[curr_food][1]:
            heapq.heappop(self.highest_ratings[cuisine])
            curr_rating, curr_food = self.highest_ratings[cuisine][0]

        return curr_food


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)