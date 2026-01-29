class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        answer = 0
        for battery in batteryPercentages:
            curr_battery = battery - answer
            if curr_battery > 0:
                answer += 1
        return answer