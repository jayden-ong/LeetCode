class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        num_compartments = int(math.sqrt(len(baskets)))
        answer = 0
        num_sections = (len(fruits) + num_compartments - 1) // num_compartments
        max_capacity_per_section = [0] * num_sections
        for i in range(len(fruits)):
            max_capacity_per_section[i // num_compartments] = max(max_capacity_per_section[i // num_compartments], baskets[i])
        
        for fruit in fruits:
            unplaced = 1
            for section in range(num_sections):
                if max_capacity_per_section[section] < fruit:
                    continue
                chosen = 0
                max_capacity_per_section[section] = 0
                for i in range(num_compartments):
                    curr_pos = section * num_compartments + i
                    if curr_pos < len(fruits):
                        if baskets[curr_pos] >= fruit and not chosen:
                            baskets[curr_pos] = 0
                            chosen = 1
                        max_capacity_per_section[section] = max(max_capacity_per_section[section], baskets[curr_pos])
                unplaced = 0
                break
            answer += unplaced
        return answer