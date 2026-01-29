class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        min_element = [float('inf')]
        basket1_dict = defaultdict(int)
        basket2_dict = defaultdict(int)
        require_swapping = []
        def valid():
            fruits_dict = defaultdict(int)
            for num in basket1:
                fruits_dict[num] += 1
                basket1_dict[num] += 1
                min_element[0] = min(min_element[0], num)

            for num in basket2:
                fruits_dict[num] += 1 
                basket2_dict[num] += 1
                min_element[0] = min(min_element[0], num)
            
            for fruit in fruits_dict:
                if fruits_dict[fruit] % 2 == 1:
                    return False
                
                if basket1_dict[fruit] != basket2_dict[fruit]:
                    for i in range((max(basket1_dict[fruit], basket2_dict[fruit]) - min(basket1_dict[fruit], basket2_dict[fruit])) // 2):
                        require_swapping.append(fruit)
            return True
        
        if not valid():
            return -1
        require_swapping.sort()
        answer = 0
        for i in range(len(require_swapping) // 2):
            answer += min(2 * min_element[0], require_swapping[i])
        return answer
