class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        power = []
        station_heap = []
        curr_power = 0
        for i, station in enumerate(stations):
            if station_heap and i - station_heap[0][0] > r:
                _, lost_power = heapq.heappop(station_heap)
                curr_power -= lost_power
            curr_power += station
            power.append(curr_power)
            heapq.heappush(station_heap, (i, station))
        
        station_heap = []
        curr_power = 0
        for i, station in enumerate(stations[::-1]):
            if station_heap and i - station_heap[0][0] > r:
                _, lost_power = heapq.heappop(station_heap)
                curr_power -= lost_power
            power[len(power) - i - 1] += curr_power
            curr_power += station 
            heapq.heappush(station_heap, (i, station))

        # We want to boost up the city with the lowest power
        def validate(min_power):
            addition_power_heap = []
            curr_add_power = 0
            curr_k = k
            for i, city in enumerate(power):
                if addition_power_heap and i - addition_power_heap[0][0] > r:
                    _, power_lost = heapq.heappop(addition_power_heap)
                    curr_add_power -= power_lost
                
                if city + curr_add_power < min_power:
                    required_power = min_power - city - curr_add_power
                    if curr_k < required_power:
                        return False
                    curr_add_power += required_power
                    curr_k -= required_power
                    heapq.heappush(addition_power_heap, (i + r, required_power))
            return True

        # Use binary search to figure out what the highest min power is
        
        left = min(power)
        right = max(power) + k
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            if validate(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return answer