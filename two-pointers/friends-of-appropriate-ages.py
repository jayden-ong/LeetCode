class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # Will not send a friend request to anyone older
        # Will not send a friend request if the other person is over 100 and the person isn't
        # age[y] <= 0.5 * age[x] + 7

        # Want to collect all of the people and how many people have a particular age
        ages_heap = []
        ages_dict = {}
        for age in ages:
            if age in ages_dict:
                ages_dict[age] += 1
            else:
                ages_dict[age] = 1
        
        for age in ages_dict:
            heapq.heappush(ages_heap, (age, ages_dict[age]))
        
        answer = 0
        previous_people = []
        while ages_heap:
            # Do not have to worry above ages[y] > ages[x] condition
            # age[y] > 100 and age[x] < 100 is covered by the second condition
            # Only have to check first condition
            curr_age, num_people = heapq.heappop(ages_heap)
            if num_people > 1 and curr_age > ((0.5 * curr_age) + 7):
                answer += (num_people) * (num_people - 1)
            
            for i in range(len(previous_people) - 1, -1, -1):
                if previous_people[i][0] <= ((0.5 * curr_age) + 7):
                    break
                else:
                    answer += num_people * previous_people[i][1]
            previous_people.append((curr_age, num_people))
        return answer
        