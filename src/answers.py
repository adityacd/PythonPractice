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

#Solution 6
nums = [1, 2, 3, -7, 8, 100, -79, 333, 12, -18, 93]

def positive(nums):
    print([x for x in nums if x > 0])

positive(nums)

#Solution 7
nums = [1, 2, 3, -7, 8, 100, -79, 333, 12, -18, 93]

def selective_stringify_nums(nums):
    print([str(x) for x in nums])

selective_stringify_nums(nums)

#Solution 8
text = 'the quick brown fox jumps over the lazy dog'

def words_not_the(text):
    print([len(x) for x in [word for word in text.split()] if x != 'the'])

words_not_the(text)

#Solution 9
text = 'mathematics'

def vowels(text):
    vow = ['a', 'e', 'i', 'o', 'u']
    print([x for x in text if x in vow])

vowels(text)