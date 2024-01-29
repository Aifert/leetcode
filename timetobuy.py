# best time to buy stock (Easy)


def maxProfit(prices):
    max_num = max(prices)
    min_num = min(prices)
    profit = 0
    loop = True

    while len(prices) != 1 or loop:
        if prices.index(max_num) > prices.index(min_num):
            profit = max_num - min_num
            loop = False
        prices.remove(max_num)
        max_num = max(prices)

    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
