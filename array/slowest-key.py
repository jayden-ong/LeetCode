class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        num_release_times = len(releaseTimes)
        answer = keysPressed[0]
        duration = releaseTimes[0]
        for i in range(1, num_release_times):
            if releaseTimes[i] - releaseTimes[i - 1] > duration:
                answer = keysPressed[i]
                duration = releaseTimes[i] - releaseTimes[i - 1]   
            elif releaseTimes[i] - releaseTimes[i - 1] == duration:
                answer = max(keysPressed[i], answer)
        return answer
