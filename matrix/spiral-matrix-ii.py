class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        temp_row = [0] * n
        answer = []
        for i in range(n):
            answer.append(temp_row.copy())
            
        # Want a variable that represents the limit
        left_wall = 0
        right_wall = n - 1
        top_wall = 0
        bottom_wall = n - 1
        curr_num = 1
        while curr_num <= n * n:
            # Going right
            for i in range(left_wall, right_wall + 1):
                answer[top_wall][i] = curr_num
                curr_num += 1
            
            if curr_num > n * n:
                break
            top_wall += 1

            #print(answer)
            # Going down
            for j in range(top_wall, bottom_wall + 1):
                answer[j][right_wall] = curr_num
                curr_num += 1
            
            if curr_num > n * n:
                break
            right_wall -= 1
            
            #print(answer)
            # Going left
            for i in range(right_wall, left_wall - 1, -1):
                answer[bottom_wall][i] = curr_num
                curr_num += 1
            
            if curr_num > n * n:
                break
            bottom_wall -= 1

            #print(answer)
            # Going up
            for j in range(bottom_wall, top_wall - 1, -1):
                answer[j][left_wall] = curr_num
                curr_num += 1
            
            #print(answer)
            left_wall += 1
        return answer