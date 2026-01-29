class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def find_common_factor(nums):
            smallest_val = min(nums)
            #print(smallest_val)
            if smallest_val <= 1:
                return False
            
            for i in range(2, (smallest_val // 2) + 1):
                satisfied = True
                for num in nums:
                    if num % i != 0:
                        satisfied = False
                        break
                if satisfied:
                    return True
            
            # Have to check smallest num itself
            for num in nums:
                satisfied = True
                if num % smallest_val != 0:
                    satisfied = False
                    break
            
            return satisfied
        # All cards have to show up more than once and must have a common factor
        card_dict = {}
        for card in deck:
            if card in card_dict:
                card_dict[card] += 1
            else:
                card_dict[card] = 1
        
        curr_amount = None
        freq_list = card_dict.values()
        #print(freq_list)
        return find_common_factor(freq_list)