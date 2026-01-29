from collections import deque
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dp_dict = {}
        key_length = len(key)
        ring_length = len(ring)
        # Dictionary will contain shortest path to each key[i]
        # The maximum number of rotations to get to all letters must be ring_length // 2
        for i in range(key_length):
            # First index represents jumping off point, second index represents number of steps
            if i == 0:
                prev_char_dict = {0 : 0}
            else:
                prev_char_dict = dp_dict[i - 1]
            
            curr_dict = {}
            for curr_key in prev_char_dict:
                # Each dict will store a list that contains the index of the letter at key[i]
                # and the min number of steps to get there
                starting_index = curr_key
                num_steps = prev_char_dict[curr_key]
                left = starting_index
                right = starting_index
                curr_steps = 0
                while curr_steps <= ring_length // 2:
                    if ring[left] == key[i]:
                        if left not in curr_dict:
                            curr_dict[left] = curr_steps + num_steps
                        else:
                            curr_dict[left] = min(curr_dict[left], curr_steps + num_steps)
                    if left == 0:
                        left = ring_length - 1
                    else:
                        left -= 1
                    
                    # Want to make sure we don't hit the same character twice
                    if ring[right] == key[i]:
                        if right not in curr_dict:
                            curr_dict[right] = curr_steps + num_steps
                        else:
                            curr_dict[right] = min(curr_dict[right], curr_steps + num_steps)

                    if right == ring_length - 1:
                        right = 0
                    else:
                        right += 1
                    curr_steps += 1
            # Assume all indices have been added
            dp_dict[i] = curr_dict.copy()
            print(curr_dict)            

        curr_answer = float('inf')
        #print(dp_dict[key_length - 2])
        for key in dp_dict[key_length - 1]:
            curr_answer = min(dp_dict[key_length - 1][key], curr_answer)
        return curr_answer + key_length
        # Have to add number of characters in key at the end