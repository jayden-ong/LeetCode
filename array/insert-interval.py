class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        already_added = False
        i = 0
        while i < len(intervals):
            interval = intervals[i]
            if not already_added and ((newInterval[0] <= interval[1] and interval[0] <= newInterval[1]) or interval[0] <= newInterval[1] <= interval[1]):
                # Need to look at next interval if it exists
                if i + 1 < len(intervals) and newInterval[1] >= intervals[i + 1][0]:
                    starting_point = min(interval[0], newInterval[0])
                    while i + 1 < len(intervals) and newInterval[1] >= intervals[i + 1][0]:
                        i += 1
                    
                    ending_point = max(intervals[i][1], newInterval[1])
                    answer.append([starting_point, ending_point])
                else:
                    interval[0] = min(interval[0], newInterval[0])
                    interval[1] = max(interval[1], newInterval[1])
                    answer.append(interval)
                already_added = True
            elif not already_added and newInterval[1] < interval[0]:
                answer.append(newInterval)
                answer.append(interval)
                already_added = True
            else:
                answer.append(interval)
            i += 1
        
        if not already_added:
            answer.append(newInterval)
        
        return answer