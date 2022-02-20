class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        min_ways = [0] + [float('inf') for _ in range(amount)]
        for current_amount in range(1, amount+1):
            for coin in coins:
                if current_amount - coin >=0:
                    min_ways[current_amount] = min(min_ways[current_amount], min_ways[current_amount-coin]+1)
        if min_ways[-1] == float('inf'):
            return -1
        return min_ways[-1]