class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # Check for a flush
        curr_suit = suits[0]
        is_flush = True
        for i in range(1, 5):
            if curr_suit != suits[i]:
                is_flush = False
                break
        
        if is_flush:
            return "Flush"
        
        # Check for three of a kind or pair
        card_dict = {}
        for card in ranks:
            if card in card_dict:
                card_dict[card] += 1
            else:
                card_dict[card] = 1
        
        most_alike = 1
        for card in card_dict:
            most_alike = max(most_alike, card_dict[card])
        
        if most_alike >= 3:
            return "Three of a Kind"
        elif most_alike == 2:
            return "Pair"
        return "High Card"