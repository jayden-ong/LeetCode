class Solution:
    def countCollisions(self, directions: str) -> int:
        answer = 0
        car_stack = []
        cars_right = 0
        for car in directions:    
            if not car_stack:
                if car != "L":
                    car_stack.append(car)
            else:
                if car_stack[-1] == "R" and car == "L":
                    answer += 1 + cars_right 
                    car_stack.append("S")
                elif car_stack[-1] == "S" and car == "L":
                    answer += 1
                elif car_stack[-1] == "R" and car == "S":
                    car_stack.append("S")
                    answer += cars_right
                else:
                    car_stack.append(car)
            
            if car == "R":
                cars_right += 1
            else:
                cars_right = 0
        return answer