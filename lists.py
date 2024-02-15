# List operations are carried out in-place. 
# Lists are mutable.

# Arrays and matrices are basically lists and nested lists.
# creating a 1D arrays
a_list = [1,2,3,4]
a_list = [0]*5
a_list = [0 for i in range(5)]
# creating a 2D arrays / matrices
a_matrix = [[1,2,3,4,5],[6,7,8,9,10]]
a_matrix = [[0]*5]*5
a_matrix = [[0 for i in range(5)] for j in range(5)]

# Modifying values
a_list[0] = 5
a_matrix[0][0] = 5
a_matrix[0] = [5,4,3,2,1]

# reversing a list/array
b = a[::-1]
# reversing a subarray
b = a[2:4][::-1]
# swapping two elements
a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
# avoiding indexing errors
a_list = [1,2,3] 
a[3] # error
a[3:4] # no error, but returns a list

# iteration
range(N)
# reversing, this is mostly O(1)
reversed(range(N))
# sorting, and returning a new array
sorted(a_list)


# Operations/mutations on lists
a_list[idx] = newvalue
a_list[start_idx:stop_idx:step] = newvalues
del a_list[index]
del a_list[start_idx:stop_idx:step]
a_list.append(item)
# remove all items
a_list.clear() 
# remove first occurence of item
a_list.remove(item) 
a_list.extend(iterable) 
a_list.insert(index,item)
a_list.pop(index)
a_list.pop() # to pop the last
a_list.reverse()
a_list.sort(key=None, reverse=False) #inplace
# mutating functions return none, 
# since its done in-place.

# Concatenation and Repetion. 
# concatenation
numbers = [1, 2, 3]
id(numbers)
numbers += [4, 5, 6]
id(numbers)
# id remains the same
# repetition.
letters = ['a', 'b', 'c']
letters *= 3
# produces ['a', 'b', 'c','a', 'b', 'c','a', 'b', 'c','a', 'b', 'c']
# id remains the same


# Copying Matrices. Shallow and Deep Copy. 
import copy
matrix = [[1, 2, 3], [4, 5, 6], [6, 7, 8]]
shallow_copy = copy.copy(matrix)
deep_copy = copy.deepcopy(matrix)
# following are True
id(matrix) != id(shallow_copy)
id(matrix) != id(deep_copy)
id(shallow_copy) != id(deep_copy)
id(matrix[0]) == id(shallow_copy[0])
id(matrix[0]) != id(deep_copy[0])
matrix[0][0] = 5 # affects shallow copy, not deep copy



