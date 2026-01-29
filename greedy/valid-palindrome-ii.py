class Solution:
    def validPalindrome(self, s: str) -> bool:
        num_saves = 1
        length_s = len(s)
        left = 0
        right = length_s - 1
        # Want to try left first
        can_try_left = False
        can_try_right = False
        saved_left = -1
        saved_right = -1
        while left < right:
            if s[left] != s[right]:
                if num_saves <= 0:
                    print(s[left])
                    print(s[right])
                    if not can_try_left and not can_try_right:
                        return False
                    if can_try_left and not can_try_right:
                        return False
                    if not can_try_left and can_try_right:
                        return False
                    else:
                        can_try_left = False
                        can_try_right = False
                        left = saved_left
                        right = saved_right
                else:
                    temp_left = left
                    temp_right = right
                    # Try deleting left and right
                    if s[temp_left + 1] == s[temp_right]:
                        can_try_left = True
                        left += 2
                        right -= 1
                    
                    if s[temp_left] == s[temp_right - 1] and can_try_left:
                        can_try_right = True
                        saved_right = temp_right - 2
                        saved_left = temp_left + 1
                    elif s[temp_left] == s[temp_right - 1]:
                        can_try_right = True
                        right -= 2
                        left += 1
                    
                    if not can_try_left and not can_try_right:
                        return False
                num_saves -= 1
            else:
                left += 1
                right -= 1
        return True