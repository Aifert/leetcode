def twoSum(nums, target):
    if len(nums) == 2 and sum(nums) == target:
        return [0, 1]

    indices = sorted(range(len(nums)), key=lambda k: nums[k])
    index1 = 0
    index2 = len(nums) - 1
    while index1 < index2:
        try:
            result = nums[indices[index1]] + nums[indices[index2]]
        except IndexError:
            print("No solution found")
            break
        if result < target:
            index1 += 1
        elif result > target:
            index2 -= 1
        elif result == target:
            return [indices[index1], indices[index2]]


# Other Solution


def otherTwoSum(nums, target):
    numMap = {}
    length = len(nums)

    for i in range(length):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i

    return []
