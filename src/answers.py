#Solution 1
nums = [1, 2, 3, 4, 5]

def identity(nums):
    print([x for x in nums])

identity(nums)

#Solution 2
nums = [1, 2, 4, 6, 8, 33, 78]

def doubled(nums):
    print([x * 2 for x in nums])

doubled(nums)

#Solution 3
nums = [1, 2, 4, 6, 8, 100, 78]

def squared(nums):
    print([x ** 2 for x in nums])

squared(nums)