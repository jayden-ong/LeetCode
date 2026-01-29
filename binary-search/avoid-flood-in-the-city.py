from sortedcontainers import SortedList
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dry_days = SortedList()
        last_rain_days = {}
        answer = [1] * len(rains)
        for i in range(len(rains)):
            if rains[i] == 0:
                dry_days.add(i)
            else:
                answer[i] = -1
                # need to find a previous day to make the lake dry
                if rains[i] in last_rain_days:
                    # Need to find the earliest day between the two rain days that is dry
                    smallest_index = dry_days.bisect(last_rain_days[rains[i]])
                    if smallest_index == len(dry_days):
                        return []
                    
                    answer[dry_days[smallest_index]] = rains[i]
                    dry_days.discard(dry_days[smallest_index])
                last_rain_days[rains[i]] = i
        return answer