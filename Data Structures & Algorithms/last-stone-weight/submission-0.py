class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            y = max(stones)
            y_index = stones.index(y)
            stones.pop(y_index)

            x = max(stones)
            x_index = stones.index(x)
            stones.pop(x_index)

            # if x == y, they have been removed from list

            if (x < y):
                stones.insert(y_index, y-x)
        
        if len(stones) == 1: # weight of the last remiaining stone
            return stones[0]
        return 0; # if none remain
