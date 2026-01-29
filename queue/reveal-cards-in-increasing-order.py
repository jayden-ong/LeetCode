class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck_size = len(deck)
        deck.sort()
        first_pointer = 0
        new_deck = []
        num_new_cards = 0
        if deck_size <= 2:
            return deck
        
        if deck_size % 2 == 0:
            rest_deck = self.deckRevealedIncreasing(deck[(deck_size // 2):])
            i = 0
            while num_new_cards != deck_size:
                new_deck.append(deck[first_pointer])
                first_pointer += 1
                new_deck.append(rest_deck[i])
                i += 1
                num_new_cards += 2
        else:
            end_card = True
            new_deck.append(deck[first_pointer])
            first_pointer += 1
            num_new_cards += 1
            rest_deck = self.deckRevealedIncreasing(deck[((deck_size // 2) + 1):])
            i = 0
            while num_new_cards != deck_size:
                if end_card:
                    new_deck.append(rest_deck[-1])
                    end_card = False
                else:
                    new_deck.append(rest_deck[i])
                    i += 1
                new_deck.append(deck[first_pointer])
                first_pointer += 1
                num_new_cards += 2    
        return new_deck