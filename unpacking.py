# *args and **kwargs in functions
# *args to unpack iterables
# **kwargs to unpack dictionaries, or named arguments
# * and ** are called the unpacking operator
def sum_integers(*integers):
	result = 0
	for x in integers:
		result += x
	return result
sum_integers(1,2,3,4)

def concatenate_words(**kwargs):
	sentence = ""
	for word in kwargs.values():
		sentence += word
	return sentence
concatenate_words(one="Hello ", two="World!")
# if iterating over kwargs instead of kwargs.values(), 
# it will return concatenation of the keys, and not the values.
# Order: non-default, default, *args, **kwargs

# Unpacking
# * operator can be used anywhere to unpack
# unpacking lists
a = [1,2,3,4]
print(a) # prints a list with square brackets
print(*a) # prints the contents of the list.
b = [2,3,4]
c = [*a, *b] # merged list
sum_integers(*a,*b) # is valid

# unpacking dictionaries
dict1 = {"A": 1, "B": 2}
dict2 = {"C": 3, "D": 4}
merged_dict = {**dict1, **dict2}

# unpacking a string
a = [*"Hello World"]
*a, = "Hello World"
print(a) # prints each letter separately

