# Given a number ānā, implement a method to count how many possible ways there are to express ānā as the sum of 1,
# 3, or 4.

def count_ways(n):
    dp = [0 for x in range(n + 1)]
    return count_ways_recursive(dp, n)


def count_ways_recursive(dp, n):
    if n == 0:
        return 1  # base case, we don't need to subtract any thing, so there is only one way

    if n == 1:
        return 1  # we can take subtract 1 to be left with zero, and that is the only way

    if n == 2:
        return 1  # we can subtract 1 twice to get zero and that is the only way

    if n == 3:
        return 2  # '3' can be expressed as {1, 1, 1}, {3}

    if dp[n] == 0:
        # if we subtract 1, we are left with 'n-1'
        subtract1 = count_ways_recursive(dp, n - 1)
        # if we subtract 3, we are left with 'n-3'
        subtract3 = count_ways_recursive(dp, n - 3)
        # if we subtract 4, we are left with 'n-4'
        subtract4 = count_ways_recursive(dp, n - 4)

        dp[n] = subtract1 + subtract3 + subtract4

    return dp[n]


def count_ways2(n):
    if n <= 2:
        return 1
    if n == 3:
        return 2

    dp = [0 for x in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 4]

    return dp[n]


def main():
    print(count_ways(4))
    print(count_ways(5))
    print(count_ways(6))


if __name__ == "__main__":
    main()
