class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        secret_count = [0] * 10
        guess_count = [0] * 10

        # First pass: count bulls and track unmatched digits
        for s_digit, g_digit in zip(secret, guess):
            if s_digit == g_digit:
                bulls += 1
            else:
                secret_count[int(s_digit)] += 1
                guess_count[int(g_digit)] += 1

        # Second pass: count cows
        cows = sum(min(secret_count[i], guess_count[i]) for i in range(10))

        return f"{bulls}A{cows}B"
