class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        bob_candies_dict = {}
        alice_candies_dict = {}
        alice_candies = 0
        bob_candies = 0

        for candy in aliceSizes:
            if candy in alice_candies_dict:
                alice_candies_dict[candy] += 1
            else:
                alice_candies_dict[candy] = 1
            alice_candies += candy
        
        for candy in bobSizes:
            if candy in bob_candies_dict:
                bob_candies_dict[candy] += 1
            else:
                bob_candies_dict[candy] = 1
            bob_candies += candy

        diff = bob_candies - alice_candies
        # If diff is < 0, alice must give up larger box
        if diff < 0:
            # For example, if diff is -2, alice must give up larger box and diff between boxes
            # must be diff // 2
            required_diff = abs(diff) // 2
            for candy in bobSizes:
                if candy + required_diff in alice_candies_dict:
                    return [candy + required_diff, candy]
        else:
        # If diff is > 0, bob must give up larger box
            required_diff = abs(diff) // 2
            for candy in aliceSizes:
                if candy + required_diff in bob_candies_dict:
                    return [candy, candy + required_diff]