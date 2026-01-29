class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        float_error = 10 ** -9
        def calculate(curr_cards):
            if len(curr_cards) == 1:
                return abs(curr_cards[0] - 24.0) <= float_error
            
            for i in range(len(curr_cards)):
                for j in range(i + 1, len(curr_cards)):
                    next_cards = []
                    for k in range(len(curr_cards)):
                        if k != i and k != j:
                            next_cards.append(curr_cards[k])
                    
                    new_card = [curr_cards[i] + curr_cards[j], curr_cards[i] - curr_cards[j], curr_cards[i] * curr_cards[j], curr_cards[j] - curr_cards[i]]
                    if curr_cards[i] != 0:
                        new_card.append(curr_cards[j] / curr_cards[i])
                    if curr_cards[j] != 0:
                        new_card.append(curr_cards[i] / curr_cards[j])
                    
                    for card in new_card:
                        if calculate(next_cards + [card]):
                            return True
            return False
        return calculate(cards)