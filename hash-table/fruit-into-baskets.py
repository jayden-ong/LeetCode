class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Keep track of streak of two fruits
        # Once we encounter a third fruit, streak ends and starts with that third fruit
        curr_fruit = fruits[0]
        curr = 1
        fruits_list = []
        for i in range(1, len(fruits) + 1):
            if i == len(fruits):
                fruits_list.append((curr_fruit, curr))
            else:
                if fruits[i] == curr_fruit:
                    curr += 1
                else:
                    fruits_list.append((curr_fruit, curr))
                    curr_fruit = fruits[i]
                    curr = 1
        
        answer = 0
        if len(fruits_list) < 2:
            return len(fruits)
        
        first_fruit, num_first_fruit = fruits_list[0]
        second_fruit, num_second_fruit = fruits_list[1]
        answer = max(answer, num_first_fruit + num_second_fruit)
        for i in range(2, len(fruits_list)):
            curr_fruit, curr_amount = fruits_list[i]
            if curr_fruit == first_fruit:
                num_first_fruit += curr_amount
            elif curr_fruit == second_fruit:
                num_second_fruit += curr_amount
            else:
                if fruits_list[i - 1][0] == second_fruit:
                    first_fruit = second_fruit
                
                num_first_fruit = fruits_list[i - 1][1]
                second_fruit, num_second_fruit = curr_fruit, curr_amount
            answer = max(answer, num_first_fruit + num_second_fruit)
        return answer