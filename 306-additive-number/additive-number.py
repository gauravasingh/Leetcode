class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        # Helper to perform string-based addition
        def add_strings(x: str, y: str) -> str:
            res = []
            carry = 0
            i, j = len(x) - 1, len(y) - 1
            while i >= 0 or j >= 0 or carry:
                digit_sum = carry
                if i >= 0:
                    digit_sum += ord(x[i]) - ord('0')
                    i -= 1
                if j >= 0:
                    digit_sum += ord(y[j]) - ord('0')
                    j -= 1
                carry, digit = divmod(digit_sum, 10)
                res.append(str(digit))
            return ''.join(reversed(res))

        # Try all splits for first and second number
        for i in range(1, n):
            for j in range(i + 1, n):
                a, b = num[:i], num[i:j]

                # Skip leading zeros
                if (len(a) > 1 and a[0] == '0') or (len(b) > 1 and b[0] == '0'):
                    continue

                start = j
                # Build sequence and match step by step
                while start < n:
                    c = add_strings(a, b)
                    if not num.startswith(c, start):
                        break
                    start += len(c)
                    a, b = b, c

                if start == n:
                    return True

        return False
