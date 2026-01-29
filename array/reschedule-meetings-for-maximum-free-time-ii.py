class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = []
        gaps_heap = []
        gaps.append(startTime[0])
        heapq.heappush(gaps_heap, (-gaps[-1], 0))
        for i in range(len(startTime) - 1):
            gaps.append(startTime[i + 1] - endTime[i])
            heapq.heappush(gaps_heap, (-gaps[-1], i + 1))
        gaps.append(eventTime - endTime[-1])
        heapq.heappush(gaps_heap, (-gaps[-1], len(gaps) - 1))

        answer = 0
        print(gaps)
        print(gaps_heap)
        # Ideally, we move the meeting to a time that is not within the break to maximize it
        for i in range(len(startTime)):
            # Index i and i + 1 are the gaps surrounding the task
            # If we can move it to a gap outside of these two, our optimal break is their sum
            # Otherwise, sum the gaps without the task time
            task_time = endTime[i] - startTime[i]
            # Only need to check 3 at most because the worst case is that the two biggest gaps
            # are the two surrounding the task and the next gap is or isn't
            temp = []
            diff_gap = False
            while gaps_heap and -gaps_heap[0][0] >= task_time:
                if i <= gaps_heap[0][1] <= i + 1:
                    temp.append(heapq.heappop(gaps_heap))
                else:
                    diff_gap = True
                    break
            
            for pair in temp:
                heapq.heappush(gaps_heap, pair)
            
            if diff_gap:
                answer = max(answer, gaps[i] + gaps[i + 1] + task_time)
            else:
                answer = max(answer, gaps[i] + gaps[i + 1])
        return answer