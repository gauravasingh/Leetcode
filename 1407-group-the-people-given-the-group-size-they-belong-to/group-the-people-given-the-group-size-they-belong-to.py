class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}   # maps group size -> list of people currently collected
        result = []

        for person, size in enumerate(groupSizes):
            if size not in groups:
                groups[size] = []
            groups[size].append(person)

            #If enough people for a complete group then  adding  it to result
            if len(groups[size]) == size:
                result.append(groups[size])
                groups[size] = []  # reset for next possible group of same size

        return result
