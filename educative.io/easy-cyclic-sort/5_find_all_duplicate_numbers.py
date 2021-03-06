# We are given an unsorted array containing ānā numbers taken from the range 1 to ānā.
# The array has some numbers appearing twice, find all these duplicate numbers without using any extra space.
#
# Example 1:
#
# Input: [3, 4, 4, 5, 5]
# Output: [4, 5]
# Example 2:
#
# Input: [5, 4, 7, 2, 3, 5, 3]
# Output: [3, 5]

def find_all_duplicates(nums):
    i = 0
    while i < len(nums):
        adjusted_index = nums[i] - 1
        if nums[i] != nums[adjusted_index]:
            nums[i], nums[adjusted_index] = nums[adjusted_index], nums[i]
        else:
            i += 1
    print(nums)
    duplicate_numbers = []
    for i in range(len(nums)):
        if nums[i] != i+1:
            duplicate_numbers.append(nums[i])

    return duplicate_numbers


def main():
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


if __name__ == "__main__":
    main()
