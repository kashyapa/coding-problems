# We are given an unsorted array containing ān+1ā numbers taken from the range 1 to ānā.
# The array has only one duplicate but it can be repeated multiple times. Find that duplicate number without using any
# extra space. You are, however, allowed to modify the input array.

# Example 1:
#
# Input: [1, 4, 4, 3, 2]
# Output: 4
# Example 2:
#
# Input: [2, 1, 3, 3, 5, 4]
# Output: 3
# Example 3:
#
# Input: [2, 4, 1, 4, 4]
# Output: 4


def find_duplicate(nums):

    i = 0
    while i < len(nums):
        adjusted_index = nums[i] - 1
        if nums[i] != nums[adjusted_index]:
            nums[i], nums[adjusted_index] = nums[adjusted_index], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i+1:
            return nums[i]

    return -1


def main():
    print(find_duplicate([1, 4, 4, 3, 2]))
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    print(find_duplicate([2, 4, 1, 4, 4]))


if __name__ == "__main__":
    main()
