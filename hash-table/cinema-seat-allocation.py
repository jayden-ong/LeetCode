class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats_set = set()
        for (row, seat) in reservedSeats:
            seats_set.add((row, seat))

        def check_first_block(row):
            for i in range(2, 6):
                if (row, i) in seats_set:
                    return False
            return True
        
        def check_second_block(row):
            for i in range(4, 8):
                if (row, i) in seats_set:
                    return False
            return True
        
        def check_third_block(row):
            for i in range(6, 10):
                if (row, i) in seats_set:
                    return False
            return True

        answer = 0
        for i in range(1, n + 1):
            if check_first_block(i) and check_third_block(i):
                answer += 2
            elif check_first_block(i) or check_second_block(i) or check_third_block(i):
                answer += 1
        return answer