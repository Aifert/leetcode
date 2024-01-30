# Single number (easy)


# def singleNumber(nums):
#     h_map = {1: []}
#     for number in nums:
#         if number in h_map[1]:
#             h_map[1].remove(number)
#         else:
#             h_map[1].append(number)

#     return h_map[1][0]


# Leetcode solution
# ^= is the XOR operator which means if there exists two numbers of the same inside
# then it will cancel each other out and leave nothing
# the one without anything to cancel will be left for num
# using bits
#   10   (binary representation of 2)
# X 01   (binary representation of 1)
# -----
#   11   (result of XOR: binary representation of 3)


def singleNumber(nums):
    num = 0
    for idx in nums:
        num ^= idx
    return num


print(singleNumber([1]))
