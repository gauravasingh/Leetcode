class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        
        # Extract vowels from s
        extracted = [ch for ch in s if ch in vowels]
        # Sort extracted vowels by ASCII
        extracted.sort()
        
        # Iterator for sorted vowels
        it = iter(extracted)
        
        # Eesult is built using sorted vowels in vowel positions
        result = []
        for ch in s:
            if ch in vowels:
                result.append(next(it))
            else:
                result.append(ch)
        
        return "".join(result)
