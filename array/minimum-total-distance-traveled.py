class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        answers_dict = {}
        def recursive_pick(robot_index, factory_index):
            if robot_index == len(robot):
                return 0
            
            if factory_index == len(factory):
                return float('inf')

            if (robot_index, factory_index, factory[factory_index][1]) in answers_dict:
                return answers_dict[(robot_index, factory_index, factory[factory_index][1])]
            
            factory_position, factory_limit = factory[factory_index]
            first_option = float('inf')
            second_option = float('inf')
            # First option - pair current factory with current index
            if factory_limit > 0:
                factory[factory_index][1] -= 1
                first_option = abs(factory_position - robot[robot_index]) + recursive_pick(robot_index + 1, factory_index)
                factory[factory_index][1] += 1

            # Second option - skip factory
            second_option = recursive_pick(robot_index, factory_index + 1)

            answer = min(first_option, second_option)
            answers_dict[(robot_index, factory_index, factory[factory_index][1])] = answer
            return answer

        answer = recursive_pick(0, 0)
        return answer