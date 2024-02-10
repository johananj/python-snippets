# Lambda functions
# bytecode for normal functions and lamda functions are same, provided same implementation. 

#function that takes x as a parameter, and returns the same.
lambda x: x 

#function that adds one to its parameter x.
lambda x: x + 1 

#calling the function with its parameter. immediately invoked function execution (IIFE).
(lambda x: x + 1)(2) 

#assigning a function to a variable
add_one = lambda x: x + 1 

#function with multiple parameters
lambda x, y: x + y 

#calling a function with multiple parameters
(lambda x, y: x + y)(2, 3) 

#function that takes a function as a parameter.
high_ord_func = lambda x, func: x + func(x) 

#calling such a nested function.
high_ord_func(2, lambda x: x * x) 

#using args
(lambda *args: sum(args))(1,2,3) 

#using kwargs
(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3) 
