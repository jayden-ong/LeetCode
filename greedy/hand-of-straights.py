class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        smallest = float('inf')
        cards_dict = {}
        card_heap = []
        for card in hand:
            if card in cards_dict:
                cards_dict[card] += 1
            else:
                cards_dict[card] = 1
                heapq.heappush(card_heap, card)
            smallest = min(smallest, card)
        
        cards_used = 0
        hand_size = len(hand)
        while cards_used < hand_size:
            curr_card = heapq.heappop(card_heap)
            while card_heap and cards_dict[curr_card] == 0:
                curr_card = heapq.heappop(card_heap)

            if cards_dict[curr_card] == 0 and not card_heap:
                return False
            
            if cards_dict[curr_card] > 1:
                heapq.heappush(card_heap, curr_card)
            cards_dict[curr_card] -= 1
            cards_used += 1
            for i in range(groupSize - 1):
                curr_card += 1
                if curr_card not in cards_dict or cards_dict[curr_card] == 0:
                    return False
                cards_dict[curr_card] -= 1
                cards_used += 1

        return True
        