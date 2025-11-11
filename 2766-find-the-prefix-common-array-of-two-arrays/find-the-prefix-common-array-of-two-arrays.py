class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seenA, seenB = set(), set()
        result = []
        common = 0

        for i in range(len(A)):
            a, b = A[i], B[i]
            seenA.add(a)
            seenB.add(b)

            # If this element is in both sets-> increase count
            if a in seenB:
                common += 1
            if b in seenA and a != b:
                common += 1

            result.append(common)

        return result
