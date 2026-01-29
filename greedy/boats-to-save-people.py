class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        num_people = len(people)
        left = 0
        right = num_people - 1
        answer = 0
        while left <= right:
            if left == right:
                answer += 1
                left += 1
            else:
                if people[left] + people[right] <= limit:
                    answer += 1
                    left += 1
                    right -= 1
                else:
                    answer += 1
                    right -= 1
        return answer