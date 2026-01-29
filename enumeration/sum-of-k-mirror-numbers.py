class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(num):
            answer = ""
            while num > 0:
                answer += str(num % k)
                num //= k
            return answer[::-1] == answer
        start = 1
        answer = 0
        while n > 0:
            end = start * 10
            for i in range(2):
                for j in range(start, end):
                    if n == 0:
                        return answer
                    
                    palindrome = j
                    if i == 0:
                        curr_num = j // 10
                    else:
                        curr_num = j
                    while curr_num > 0:
                        palindrome = palindrome * 10 + curr_num % 10
                        curr_num //= 10
                    
                    if is_palindrome(palindrome):
                        n -= 1
                        answer += palindrome
            start = end
        return answer