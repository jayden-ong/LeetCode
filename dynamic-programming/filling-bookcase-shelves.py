class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # Want to use dp
        # At each step, the options are to put the book on a new shelf or continue
        dp = [0] * len(books)
        for i in range(len(books) - 1, -1, -1):
            curr_thick, curr_height = books[i]
            if i == len(books) - 1:
                dp[i] = curr_height
            else:
                # We need to decide when the next book is going to a new shelf
                possible_answers = []
                total_width = curr_thick
                max_height = curr_height
                too_wide = False
                for j in range(i + 1, len(books)):
                    # Next book is forced to a new shelf
                    possible_answers.append(max_height + dp[j])
                    if curr_thick + books[j][0] > shelfWidth:
                        too_wide = True
                        break
                    else:
                        # The current shelf height might expand when new book is added
                        max_height = max(max_height, books[j][1])
                        curr_thick += books[j][0]
                
                if not too_wide:
                    possible_answers.append(max_height)
                
                dp[i] = min(possible_answers)
        return dp[0]
