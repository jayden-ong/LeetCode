class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        open_block_line = False
        answer = []
        # Only want to append to answer if there is no open block line
        curr_line = ""
        for word in source:
            i = 0
            while i < len(word):
                if open_block_line:
                    # Need to find the next instance of */
                    location = word.find("*/", i, len(word))
                    # If it doesn't exist, skip everything and move to next word
                    # Otherwise, continue 2 after location
                    if location == -1:
                        break
                    else:
                        i = location + 2
                        open_block_line = False
                else:
                    # If we see a line level comment, rest of line is void
                    # If we see a block level, need to adjust
                    if i + 1 < len(word):
                        if word[i:i + 2] == "//":
                            break
                        elif word[i:i + 2] == "/*":
                            open_block_line = True
                            i = i + 2
                        else:
                            curr_line += word[i]
                            i += 1
                    else:
                        curr_line += word[i]
                        i += 1
            if not open_block_line and curr_line != "":
                answer.append(curr_line)
                curr_line = ""
        return answer
