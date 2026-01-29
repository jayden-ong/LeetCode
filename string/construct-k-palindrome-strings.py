class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # Each palindrome has to have at least one character in it
        # If we want k palindromes, just put each letter in its own string
        if k > len(s):
            return False
        elif k == len(s):
            return True
        
        # In order to form a palindrome, you have to have an even amount of all but one of the letters
        num_even = 0
        num_odd = 0
        letters_dict = defaultdict(int)
        for letter in s:
            letters_dict[letter] += 1
            if letters_dict[letter] == 1:
                num_odd += 1
            elif letters_dict[letter] % 2 == 1:
                num_odd += 1
                num_even -= 1
            else:
                num_even += 1
                num_odd -= 1
        
        # Want to count the minimum number of palindromes that have to be constructed
        # Each letter that appears an odd amount of times can be paired with a letter that appears an even amount 
        # of times to form one palindrome
        min_palindromes = 0
        num_pairs = min(num_even, num_odd)
        num_even -= num_pairs
        num_odd -= num_pairs
        min_palindromes += num_pairs
        # If num_even > 0, we can combine them all together
        # We only increment if we have not formed a palindrome yet. In the other case, we can just add the letters
        # to the prexisting palindrome.
        if num_even > 0:
            if min_palindromes == 0:
                min_palindromes += 1
        
        # If num_odd > 0, each letter has to go in its own string
        if num_odd > 0:
            min_palindromes += num_odd

        return min_palindromes <= k