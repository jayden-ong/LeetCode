class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        blocks = [('1', 1)]
        active = 0
        if s[0] == '1':
            active += 1
        
        curr_block = 1
        num_behind = 0
        curr, curr_count = s[0], 1
        index_to_block_num_behind = [(1, 0)]
        for i in range(1, len(s)):
            if s[i] == curr:
                curr_count += 1
                num_behind += 1
            else:
                num_behind = 0
                curr_block += 1
                blocks.append((curr, curr_count))
                curr = s[i]
                curr_count = 1
            index_to_block_num_behind.append((curr_block, num_behind))
            if s[i] == '1':
                active += 1
        blocks.append((curr, curr_count))
        blocks.append(('1', 1))
        def get_sub_blocks(left, right):
            curr_left_block = blocks[index_to_block_num_behind[left][0]]
            curr_right_block = blocks[index_to_block_num_behind[right][0]]
            if index_to_block_num_behind[left][0] == index_to_block_num_behind[right][0]:
                return [('1', 1), (curr_left_block[0], curr_right_block[1] - curr_left_block[1]), ('1', 1)]
            else:
                new_left_block = (curr_left_block[0], curr_left_block[1] - index_to_block_num_behind[left][1])
                new_right_block = (curr_right_block[0], index_to_block_num_behind[right][1] + 1)
                if index_to_block_num_behind[right][0] - index_to_block_num_behind[left][0] == 1:
                    return [('1', 1), new_left_block, new_right_block, ('1', 1)]
                curr = [('1', 1), new_left_block]
                for i in range(index_to_block_num_behind[left][0] + 1, index_to_block_num_behind[right][0]):
                    curr.append(blocks[i])
                curr.append(new_right_block)
                curr.append(('1', 1))
                return curr

        def solve(blocks):
            if len(blocks) <= 4 or len(blocks) == 5 and blocks[1][0] == '1':
                return active
            answer = 0
            actual_start = 2
            if blocks[1][0] == '1':
                actual_start = 3
            for i in range(actual_start, len(blocks) - 2, 2):
                answer = max(answer, active + blocks[i - 1][1] + blocks[i + 1][1])
            return answer

        answers_dict = {}
        answer = []
        for left, right in queries:
            if (left, right) not in answers_dict:
                sub_blocks = get_sub_blocks(left, right)
                answers_dict[(left, right)] = solve(sub_blocks)
            answer.append(answers_dict[(left, right)])
        return answer