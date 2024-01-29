# best time to buy stock (Easy)


def maxProfit(prices):
    max_num = max(prices)
    min_num = min(prices)
    profit = 0
    loop = True

    while loop:
        if len(prices) != 1:
            if prices.index(min_num) == len(prices) - 1:
                prices.remove(min_num)
                min_num = min(prices)
            elif prices.index(max_num) > prices.index(min_num):
                profit = max_num - min_num
                loop = False
            else:
                prices.remove(max_num)
                max_num = max(prices)
        else:
            loop = False

    return profit


print(maxProfit([3, 2, 6, 5, 0, 3]))
