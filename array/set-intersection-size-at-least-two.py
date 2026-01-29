class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[1], -x[0]))
        print(intervals)
        # Add the two greatest numbers in the interval range
        # Let's say the first interval is 1, 2
        #   If the next interval starts with 1, we are guaranteed covered -- interval is satisfied
        #   If it doesn't then we could not have done better
        answer = 0
        first_num, last_num = None, None
        for i, (start, end) in enumerate(intervals):
            # The interval is impossible to satisfy without adding the two greatest nums in the interval
            if i == 0:
                answer += 2
                first_num, last_num = end - 1, end
                continue
            
            # This interval is already satisifed
            if start <= first_num <= last_num <= end:
                continue
            elif first_num < start and last_num < start:
                first_num, last_num = end - 1, end
                answer += 2
            elif first_num < start and last_num >= start:
                first_num, last_num = last_num, end
                answer += 1
        return answer