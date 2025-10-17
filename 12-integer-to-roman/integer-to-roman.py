class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        roman_parts = []
        val_sym_pairs = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

        for val, sym in val_sym_pairs:
            count, num = divmod(num, val)
            roman_parts.append(sym * count)

        return ''.join(roman_parts)

        