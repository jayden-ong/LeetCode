class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()
        # If you choose to use a certain power spell, you can use any spell with that same power
        
        # Want to keep track of the largest index of the spell that can be used
        best_prev_spell = [-1] * len(power)
        spell_heap = []
        for i in range(len(power)):
            if i > 0 and power[i] == power[i - 1]:
                best_prev_spell[i] = best_prev_spell[i - 1]
            
            prev_spell, prev_index = None, None
            while spell_heap and spell_heap[0][0] <= power[i] - 3:
                prev_spell, prev_index = heapq.heappop(spell_heap)
                best_prev_spell[i] = prev_index
            
            # Might need to use it in the future
            if prev_spell is not None:
                heapq.heappush(spell_heap, (prev_spell, prev_index))
            
            heapq.heappush(spell_heap, (power[i], i))
        
        # First index is best answer, if you had to use that spell
        # Second index is general best answer
        dp = [[0, 0] for i in range(len(power))]
        for i in range(len(power)):
            # If it has the same power, can use that spell
            if i > 0 and power[i - 1] == power[i]:
                dp[i][0] = dp[i - 1][0] + power[i]
            elif best_prev_spell[i] == -1:
                dp[i][0] = power[i]
            else:
                dp[i][0] = power[i] + max(dp[best_prev_spell[i]][0], dp[best_prev_spell[i]][1])
            dp[i][1] = max(dp[i][0], dp[i - 1][1])
            
        #print(power)
        #print(dp)
        return dp[-1][1]