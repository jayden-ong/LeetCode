class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def determine_closest_power(x):
            i = 0
            while True:
                if pow(3, i) > x:
                    return i - 1
                i += 1
        
        curr = n
        prev_power = None
        while True:
            closest_power = determine_closest_power(curr)
            if prev_power is not None and closest_power >= prev_power:
                closest_power = prev_power - 1
            
            if pow(3, closest_power) == curr:
                return True
            
            if closest_power == 0:
                return False
            curr -= pow(3, closest_power)
            prev_power = closest_power
        # Will never run
        return False
            