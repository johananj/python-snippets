# to define parameters types (in versions<python3.9), 
# import it first, ex:
from typing import List
# then define the function
def function_name(nums: List[int]) -> int:

# to assign value to a global variable inside a function
counter = 0
def increment():
	global counter
	counter += 1 

# Using enumerate 
# to get both idx and values at the same time. 
values = [1,2,3,4]
for idx, value in enumerate(values [, start = 1]):
	print(idx,value)

# Raising exceptions
def do_something(parameter):
	if parameter > 100:
  	raise ValueError('Parameter should...')
	# rest of the code
try:
	do_something(101)
except ValueError, e:
	# display error message if necessary e.g. print str(e)

# Building custom exception classes
class ParameterError(Exception):
	pass

# iterating over two lists in parallel
for f, b in zip(foo, bar):
	print(f, b)

# to get the next item in an iterable
mylist = iter(["apple", "banana", "cherry"])
print(next(mylist))