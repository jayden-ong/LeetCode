class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 0:
            return 0
        
        answer = [-1] * len(ratings)
        ratings_heap = []
        for i, rating in enumerate(ratings):
            heapq.heappush(ratings_heap, (rating, i))
        
        while ratings_heap:
            curr_rating, curr_index = heapq.heappop(ratings_heap)
            candy_amount = 1
            if curr_index < len(ratings) - 1:
                if answer[curr_index + 1] != -1:
                    # If the next index is not set, its rating must be at least curr_rating
                    # In that case, no need to do anything yet
                    # If it is set, the next rating must be smaller
                    candy_amount = max(candy_amount, answer[curr_index + 1] + 1)
            
            if curr_index > 0:
                if answer[curr_index - 1] != -1:
                    # The rating of the index below must be less than or equal to current rating
                    if ratings[curr_index - 1] < ratings[curr_index]:
                        candy_amount = max(candy_amount, answer[curr_index - 1] + 1)
            answer[curr_index] = candy_amount

        print(answer)
        return sum(answer)