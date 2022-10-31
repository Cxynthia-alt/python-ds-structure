# letters = list('apple')
# print(letters)

# membership operators: use in to check for membership
# nums = list(range(0, 10, 2))
# # if 2 in nums: print('yeah 2')
# # for num in [4, 5, 6]:
# #   if num not in nums:
# #     print(f'oh {num} is not in the nums list')

# last = nums[-1]
# print(f'the last num of the list is {last}')


# in js, template literal is ${}
# in python, {}
# price = 3.5
# qty = 7
# print(f"your total is {price * qty}")

# to string
# print(str([3, 4, 5]))

# dictionary
# dic = {'name': 'butter', 'age': 6, 'breed': 'Silkie'}
# stuff = {True: 34, 100: 'awesome'}
# # can use in to see if the key exists
# print('name' in dic)
# #  will return true
# # use [] to access value
# print(stuff[True])
# print(dict([[True, 0], [False, 1]]))

# looping in dictionary
chicken = {
    'name': 'Lady Gray',
    'breed': 'Silkie',
    'total_egg_count': 12,
    'egg_chart': {'M': True, 'T': True},
    'coop_mates': ['butter', 'henry']}
# for key in chicken.keys():
#     print(key)
# for value in chicken.values():
#     print(value)
# for pair in chicken.items():
#     print(pair)
# can unpack a pair within a dict
# for (key, value) in chicken.items():
#     print(key, 'is', value)
# dict method: d.get(x, default) retrieve value of x
chicken.get('sex')
# return nothing because the dict doesn't have a key named "sex"
chicken['sex'] = 'female'
# add that 'sex' key
# print(chicken.get('sex'))
# it'll return female
# {}.pop(key) remove the key and return the corresponding value


# set
# making sets with only keys using {}
# set.pop() remove and return an arbitrary set element
lemon = {'sour', 'yellow', 'fruit', 'bumpy'}
banana = {'fruit', 'yellow', 'sweet', 'smooth'}
# union banana | lemon (or banana.union(lemon))
# intersection banana & lemon (same for banana.intersection(lemon))
# difference banana - lemon (or the other way around)
# symmetric difference ^: the opposite of overlap, all the elements from 2 sets that's not an overlap. same for (lemon.symmetric_difference(banana))
# print(banana ^ lemon)
# set: iterable, combined with the operators above
# for adj in lemon:
#     print(adj)
# you can turn a list to a set
orange = ['tangerin', 'round', 'bumpy', 'sour']
# for adj in banana | lemon | set(orange):
#     print(adj)
# remove dublicates from a list
list(set([1, 3, 2, 6, 3, 1, 1, 9]))


# tuple ()
colors = ('red', 'green', 'yellow')
# if a tuple only has 1 item, use comma to let python know that it's a tuple not a parenthesis operator
tup1 = (3)
tup2 = (3,)
# print(type(tup1))  # integer
# print(type(tup2))  # tuple
# good use: it's slightly smaller, faster than lists and immutable, so they can be used as dict keys or put into sets


# list comprehension
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in nums if num % 2 == 0]
plusOne = [num+1 for num in nums]
# replace the item of a list with x
# [x for thing in list/string]
newList = [n * n for n in [2, 3, 4, 5]]
upperChar = [char.upper() + '.' for char in 'apple']
fromRange = [num for num in range(1, 5)]

# nested list using comprehension


def gen_board(size, initial_val):
    return [[initial_val for x in range(size)] for cell in range(size)]


gen_board(5, None)

# access dict data from comprehension:
people = [{'name': 'Alice', 'gender': 'female'},
          {'name': 'Ben', 'gender': 'male'},
          {'name': 'Cathy', 'gender': 'female'},
          {'name': 'Den', 'gender': 'male'}]
male = [item['name'] for item in people if item['gender'] == 'male']

# assess dict data from list comprehension:
# using if else condition: [condition A if A else condition B for item in list]
scores = [{'name': 'Alice', 'score': 99},
          {'name': 'Benja', 'score': 82},
          {'name': 'Cathy', 'score': 73},
          {'name': 'Den', 'score': 62},
          {'name': 'Ethan', 'score': 23}]
scoreList = [item['score'] for item in scores]
result = ['pass' if item > 70 else 'fail' for item in scoreList]
names = [item['name'] for item in scores]


# sort the result by get.()
# you can use [] to access the value by key from a dict, or dict.get(key)
# here we add another argument in .get(). If key doesn't exist in dict, it'll return that argument, in this case "invalid input"


def get_letter(letter):
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-'}

    return MORSE_CODE_DICT.get(letter.upper(), 'invalid input')


# if we want to get the morse code of a string, we could combine this function and list comprehension
msg = [get_letter(char) for char in 'apple']
# turn the list msg to a string


def msg_to_str(phrase):
    return ' '.join([get_letter(char) for char in phrase])


# dic & set comprehension : {}
# dict
test_dictCompre = {item: 'student' for item in names}
# set: filter for vowels/consonants
test_setCompre = {char for char in 'apple' if char in 'aeiou'}
test_setCompre_2 = {char for char in 'apple' if char not in 'aeiou'}
