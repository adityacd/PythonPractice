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

#Solution 10
text = 'mathematics'

def vowels_set(text):
    vow = ['a', 'e', 'i', 'o', 'u']
    print(list({x for x in text if x in vow}))

vowels_set(text)

#Solution 11
text = 'the quick brown fox jumps over the lazy dog'

def disemvowel(text):
    vow = ['a', 'e', 'i', 'o', 'u']
    print("".join([x for x in text if x not in vow]))

disemvowel(text)

#Solution 12
nums = [72, 26, 79, 70, 20, 68, 43, -71, 71, -2]

def wiggle_numbers(nums):
    print([x*2 if x%2==0 else -x for x in nums])

wiggle_numbers(nums)

#Solution 13
text = 'the quick brown fox jumps over the lazy dog'

def encrypt_lol(text):
    # b = bytes(text, 'utf-8')
    num_array = [bytes(text, 'utf-8')[x] for x in range(0, len(bytes(text, 'utf-8')))]
    k = "".join([chr(x + 1) for x in num_array])
    print(k.replace('!', ' '))

encrypt_lol(text)