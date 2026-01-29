class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Whatever gas station we start at, the gas must be at least as high as cost
        # If you start at some station and get stuck at another station, all stations
        # in between are also invalid
        num_gas = len(gas)
        i = 0
        while i < num_gas:
            if gas[i] >= cost[i]:
                if i == num_gas - 1:
                    j = 0
                else:
                    j = i + 1
                curr_gas = gas[i] - cost[i]
                while j != i and curr_gas >= 0:
                    curr_gas += gas[j] - cost[j]
                    if curr_gas < 0:
                        break
                    if j + 1 >= num_gas:
                        j = 0
                    else:
                        j += 1
                
                if j < i:
                    return -1
                elif j == i:
                    return j
                i = j
            else:
                i += 1
        return -1