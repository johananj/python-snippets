# Basic Operations. Create. Modify. Add. Delete.
pantry_kg = {"wheat-flour": 2, "rice": 10, "moong":2}
pantry_kg["rice"] = 7
pantry_kg["sugar"] = 1
pantry_kg["salt"] # KeyError
del pantry_kg["wheat-flour"]
del pantry_kg["salt"] # KeyError

# alternate way of defining
pantry_kg = dict([("wheat-flour": 2), ("rice": 10), ("moong": 2)])
# if keys are simple strings, use as arguments
pantry_kg = dict(wheatflour = 2, rice = 10, moong= 2)

# any "immutable type" can be used as a key
# but the numbers are not indices, they are keys
d = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
# keys dont have to be of the same type as well
foo = {42: 'aaa', 2.78: 'bbb', True: 'ccc'}
# they can even be tuples
d = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}

# building up from an empty dictionary
person = {}
person["fname"] = "John"
person["age"] = 40
# values can be anything, even lists, dictionaries, and objects
person['children'] = ['Jake', 'Joke', 'Juke']
person['pets'] = {'dog': 'doggo', 'cat': 'catto'}}
# accessing the values in the sub-list stored with key 'children'
person['children'][0] # Jake
# accessing the values in the sub-dictionary stored with key 'children'
person['pets']['dog']


# keys are unique.
# same keys will override each other, with the latest value, even during creation

# check if key present. following are True
'rice' in pantry_kg
'cocoa' not in pantry_kg

# to get number of key-value pairs
len(pantry_kg)
# clear all key-value pairs
a_dict.clear()
# get value for key, if it exists, None if not found
a_dict.get(key,[default])
# get a list of key-value pairs as tuples, keys, values
a_dict.items()
a_dict.keys()
a_dict.values()
# pop the most recently added
a_dict.pop() # return value
a_dict.popitem() # return key-value tuple
# pop pair with key, return value, 
# or return default if key doesnt exist
rkey = a_dict.pop(key[,default])
# update dict with another dict
a_dict.update(another_dict)
# get value if key present, else set key-value
rvalue = a_dict.setdefault(key[,value])

# keys must be unique and hashable
# hashable - unchangeable - immutable: numbers, boolieans, strings

# merge two dictionaries
pantry_kg = {"wheat-flour": 2} | {"moong":2}
pantry_kg = {"wheat-flour": 2}
pantry_kg |= {"moong":2}
# id remains the same. 

# Compare two dictionaries
a_dict = Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1})
b_dict = Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 2, 'f': 1})
a_dict & b_dict # {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
a_dict | b_dict # {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 2, 'f': 1}




