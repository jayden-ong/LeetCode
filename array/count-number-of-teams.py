class Solution:
    def numTeams(self, rating: List[int]) -> int:
        num_length_two_increasing = [0] * len(rating)
        num_length_two_decreasing = [0] * len(rating)
        answer = 0
        # Want to figure out how many ways we can make increasing length 3
        for i in range(len(rating)):
            for j in range(i):
                # Want to figure our how many subsequences of length 2 we can make
                # We should never have to change num_length...[j]
                if rating[j] < rating[i]:
                    num_length_two_increasing[i] += 1
                    # num_length_two_increasing[j] contains number of subsequences that
                    # are increasing, are length 2, and end at index j
                    answer += num_length_two_increasing[j]
                
                if rating[j] > rating[i]:
                    num_length_two_decreasing[i] += 1
                    answer += num_length_two_decreasing[j]
        return answer
