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
