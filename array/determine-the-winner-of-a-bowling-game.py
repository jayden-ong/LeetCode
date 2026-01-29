class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        length_score_1 = len(player1)
        length_score_2 = len(player2)
        
        score1 = 0
        for i in range(length_score_1):
            if (i > 0 and player1[i - 1] == 10) or (i > 1 and player1[i - 2] == 10):
                score1 += 2 * player1[i]
            else:
                score1 += player1[i]
        
        score2 = 0
        for i in range(length_score_2):
            if (i > 0 and player2[i - 1] == 10) or (i > 1 and player2[i - 2] == 10):
                score2 += 2 * player2[i]
            else:
                score2 += player2[i]
        
        if score1 > score2:
            return 1
        elif score2 > score1:
            return 2
        return 0