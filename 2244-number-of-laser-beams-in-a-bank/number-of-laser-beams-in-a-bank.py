class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0   # No of devices in previous non-empty row
        total = 0  # total no of laser beams

        for row in bank:
            devices = row.count('1')
            if devices:  # only consider rows that have devices
                total += prev * devices
                prev = devices  # update previous non-empty row

        return total
