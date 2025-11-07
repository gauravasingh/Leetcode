class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        # Define mappings for words
        below_20 = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", 
            "Eighteen", "Nineteen"
        ]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        units = ["", "Thousand", "Million", "Billion"]

        # Helper function for numbers < 1000
        def three_digit_to_words(n):
            if n == 0:
                return ""
            elif n < 20:
                return below_20[n]
            elif n < 100:
                return tens[n // 10] + (" " + below_20[n % 10] if n % 10 != 0 else "")
            else:
                return below_20[n // 100] + " Hundred" + (" " + three_digit_to_words(n % 100) if n % 100 != 0 else "")

        # Split number into chunks of three digits
        res = []
        i = 0
        while num > 0:
            part = num % 1000
            if part != 0:
                words = three_digit_to_words(part)
                if units[i]:
                    words += " " + units[i]
                res.append(words)
            num //= 1000
            i += 1

        # Join the words in reverse order (from billions down to ones)
        return " ".join(reversed(res)).strip()
