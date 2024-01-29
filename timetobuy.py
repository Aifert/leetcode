# best time to buy stock (Easy)

# this solution is too slow

# def maxProfit(prices):
#     max_gap = 0
#     for i in range(len(prices)):
#         temp = prices[i:]
#         if (max(temp) - prices[i]) >= max_gap:
#             max_gap = max(temp) - prices[i]

#     return max_gap


# Leetcode soltion

# main idea is using two pointers left and right and checking if the right is greater than left
# if it is then check if it is greater profit than currently is


def maxProfit(prices):
    left, right = 0, 1
    max_gap = 0
    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_gap = max(max_gap, profit)
        else:
            left = right
        right += 1

    return max_gap


print(maxProfit([7, 1, 5, 3, 6, 4]))
