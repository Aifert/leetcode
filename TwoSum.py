def twoSum(nums, target):
    if len(nums) == 2:
        if sum(nums) == target:
            return [0, 1]
    index1 = 0
    index2 = int(len(nums) / 2) + 1
    while index1 != index2:
        if index1 + 1 == index2:
            index1 += 1
        try:
            result = nums[index1] + nums[index2]
        except IndexError:
            print("No solution found")
            break
        if result < target:
            index2 += 1
        elif result > target:
            index2 -= 1
        elif result == target:
            return sorted([index1, index2])


print(twoSum([2, 5, 5, 11], 10))
