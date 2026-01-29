class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        # For each standing domino, want to know closest domino to the left that is falling right
        # and closest domino to the right that is falling left
        # If the distances are equal, domino stays
        closest_falling_right = []
        curr_closest = None
        for i in range(len(dominoes)):
            domino = dominoes[i]
            if domino == ".":
                closest_falling_right.append(curr_closest)
            else:
                closest_falling_right.append(None)
                if domino == "R":
                    curr_closest = i
                else:
                    curr_closest = None
        
        closest_falling_left = []
        curr_closest = None
        for i in range(len(dominoes) - 1, -1, -1):
            domino = dominoes[i]
            if domino == ".":
                closest_falling_left.append(curr_closest)
            else:
                closest_falling_left.append(None)
                if domino == "L":
                    curr_closest = i
                else:
                    curr_closest = None
        closest_falling_left = closest_falling_left[::-1]
        
        answer = ""
        for i in range(len(dominoes)):
            if dominoes[i] == ".":
                if closest_falling_right[i] is None:
                    right_distance = float('inf')
                else:
                    right_distance = i - closest_falling_right[i]
                
                if closest_falling_left[i] is None:
                    left_distance = float('inf')
                else:
                    left_distance = closest_falling_left[i] - i
                
                if right_distance < left_distance:
                    answer += "R"
                elif left_distance < right_distance:
                    answer += "L"
                else:
                    answer += "."
            else:
                answer += dominoes[i]
        return answer
