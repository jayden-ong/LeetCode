class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        num_bulls = 0
        secret_dict = {}
        guess_dict = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                num_bulls += 1
            else:
                if secret[i] in secret_dict:
                    secret_dict[secret[i]] += 1
                else:
                    secret_dict[secret[i]] = 1
                
                if guess[i] in guess_dict:
                    guess_dict[guess[i]] += 1
                else:
                    guess_dict[guess[i]] = 1
        
        num_cows = 0
        for key in guess_dict:
            if key in secret_dict and secret_dict[key] > 0:
                num_correct = min(secret_dict[key], guess_dict[key])
                num_cows += num_correct
                secret_dict[key] -= num_correct
                guess_dict[key] -= num_correct
        
        return str(num_bulls) + "A" + str(num_cows) + "B"