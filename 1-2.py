def two_sum_bruteforce(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

nums = [3, 4, 5, 6]
target = 7
print(two_sum_bruteforce(nums, target)) 
