class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        '''
        dp_dict = {}
        for i in range(len(heights)):
            dp_dict[i] = [-1] * len(heights)
            
            curr_building = i
            for j in range(i, len(heights)):
                while curr_building < len(heights) and ((heights[i] >= heights[curr_building] and i != curr_building) or (heights[j] >= heights[curr_building] and j != curr_building)):
                    curr_building += 1
                
                # No building
                if curr_building == len(heights):
                    break
                
                dp_dict[i][j] = curr_building
                if curr_building <= j:
                    curr_building += 1
        
        answer = []
        for alice, bob in queries:
            answer.append(dp_dict[min(alice, bob)][max(alice, bob)])
        return answer
        '''

        '''
        dp = [-1] * len(heights)
        curr_building_stack = []
        for i in range(len(heights) - 1, -1, -1):
            while curr_building_stack and heights[i] >= heights[curr_building_stack[-1]]:
                curr_building_stack.pop()
            
            if curr_building_stack:
                dp[i] = curr_building_stack[-1]
            
            curr_building_stack.append(i)
        
        answer = []
        for alice, bob in queries:
            first = min(alice, bob)
            second = max(alice, bob)
            # first equals second --- stay
            # first can move into second
            # first cannot move anywhere other than to itself where second cannot move
            # -- second cannot move anywhere and first cannot move into second
            if first == second:
                answer.append(second)
            elif heights[first] < heights[second]:
                answer.append(second)
            elif dp[first] == -1 or dp[second] == -1:
                answer.append(-1)
            else:
                curr_building = max(dp[first], dp[second])
                if heights[first] < heights[curr_building] and heights[second] < heights[curr_building]:
                    answer.append(curr_building)
                else:
                    answer.append(-1)
        return answer
        '''
        answer = [-1] * len(queries)
        leftovers = defaultdict(list)
        i = 0
        for a, b in queries:
            a, b = min(a, b), max(a, b)
            if a == b or heights[a] < heights[b]:
                answer[i] = b
            else:
                leftovers[max(a, b)].append((max(heights[a], heights[b]), i))
            
            i += 1
        
        valid_queries = []
        j = 0
        for height in heights:
            while valid_queries and valid_queries[0][0] < height:
                _, curr_index = heapq.heappop(valid_queries)
                answer[curr_index] = j

            # On the table for processing
            for max_height, index in leftovers[j]:
                heapq.heappush(valid_queries, (max_height, index))
        
            j += 1
        return answer