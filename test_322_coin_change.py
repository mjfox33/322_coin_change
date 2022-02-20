from code_322_coin_change import Solution

def test_example_1():
    s = Solution()
    coins = [1,2,5]
    amount = 11
    output = 3
    assert s.coinChange(coins,amount) == output