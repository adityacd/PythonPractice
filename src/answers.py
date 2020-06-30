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

#Solution 4
nums = [1, 2, 4, 6, 8, 100, 78]

def evens(nums):
    print([x for x in nums if x % 2 == 0])

evens(nums)

#Solution 5
nums = [1, 2, 3, 7, 8, 100, 79, 333, 12, 18, 93]

def odds(nums):
    print([x for x in nums if x % 2 != 0])

odds(nums)