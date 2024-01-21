# Climbing Stairs (easy)

def climbStairs(n):
    one, two = 1 , 1
    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp
    return one

print(climbStairs(5))

# Leet code solution
# Let's take 5 as an example, 
# To get to 5 from 4, we can take 1 step only, so there is only 1 way
# To get to 5 from 3, we can take 1 step which will land us at 4, or 2 steps which will land us at 5 (2 ways)
# To get to 5 from 2, we can take 1 step which will land us at 3 (which we have already computed, 2 ways to get to 5), or take 2 steps which will land us at 4 (1 way) final (2 + 1 ways = 3)
# keep repeating that until you get from 0 and that is your answer

