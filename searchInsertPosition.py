# Search Insert Position (easy)


def searchInsert(nums, target):
    result = 0
    if target <= nums[0]:
        return 0
    elif target not in nums:
        while len(nums) != 0:
            if nums[-1] <= target:
                if result == 0:
                    return len(nums)
                else:
                    return result + len(nums)
            else:
                middle = int(len(nums) / 2)
                middle_number = nums[middle]
                if middle_number < target:
                    result += middle
                    nums = nums[middle:]
                else:
                    nums = nums[:middle]
    else:
        return nums.index(target)


print(searchInsert([2, 5], 1))


# LEET CODE ANSWERS

# Basic concept is having two pointers one at the first elemenet and one at the last element, loop through until they become the same tnumber adn that index will be the one to be inserted

# class Solution(object):
#     def searchInsert(self, nums, target):
#         l = 0
#         r = len(nums) - 1
#         while l <= r:
#             mid = (l + r) // 2
#             if nums[mid] < target:
#                 l = mid + 1
#             elif nums[mid] > target:
#                 r = mid - 1
#             else:
#                 return mid
#         return l
