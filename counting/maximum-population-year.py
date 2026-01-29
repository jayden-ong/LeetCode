class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        largest_population = 0
        answer_dict = {}
        answer = None
        for log in logs:
            for i in range(log[0], log[1]):
                if i in answer_dict:
                    answer_dict[i] += 1
                else:
                    answer_dict[i] = 1

                if answer_dict[i] > largest_population:
                    largest_population = answer_dict[i]
                    answer = i
                elif answer == i:
                    largest_population = answer_dict[i]
                elif answer_dict[i] == largest_population and i < answer:
                    answer = i
        return answer