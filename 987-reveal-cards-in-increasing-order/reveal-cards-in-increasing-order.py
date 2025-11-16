class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        from collections import deque
        
        deck.sort()
        dq = deque()
        
        # Reverse simulation: process largest → smallest
        for card in reversed(deck):
            if dq:
                dq.appendleft(dq.pop())  # move bottom to top
            dq.appendleft(card)          # place the card on top
        
        return list(dq)
