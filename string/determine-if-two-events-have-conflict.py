class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # Convert each event time to minutes
        event1_start = int(event1[0][:2]) * 60 + int(event1[0][3:])
        event1_end = int(event1[1][:2]) * 60 + int(event1[1][3:])
        event2_start = int(event2[0][:2]) * 60 + int(event2[0][3:])
        event2_end = int(event2[1][:2]) * 60 + int(event2[1][3:])
        return min(event1_end, event2_end) - max(event1_start, event2_start) >= 0