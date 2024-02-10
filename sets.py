# Mutable. 
# No order. No duplicates. No indexing. 
# A special dictionary with with only keys, instead of key-value pairs.

fruits = {"apple", "orange", "banana"}
# Common Operations on Sets
a_set.add(element)
a_set.update(*others) # like append
a_set.remove(element)
a_set.discard(element) # ignore key error
a_set.pop() # remove and return arbitrary element, keyerror if empty
a_set.clear()
# *others are other set(s) separated by comma

# Set Operations. Intersection. Difference.
# update in place. intersection wrt to other sets
a_set.intersection_update(*others)
# update in place. remove items found in others
a_set.difference_update(*others)
# not xor. keep elements found in either, and not both.
a_set.symmetric_difference_update(other)
# using symbols
{"apple", "orange"} | {"banana"}  # Union
{"apple", "orange"} & {"apple"}  # Intersection
{"apple", "orange"} - {"apple", "banana"}  # Difference
{"apple", "orange"} ^ {"apple", "banana"}  # Symmetric difference

fruits = {"apple", "orange"}
fruits |= {"banana"}  # Augmented union
fruits &= {"apple"}  # Augmented intersection

# immutable sets
fruits = frozenset(["apple", "orange", "banana"])
# but supports union, difference, intersection, symmetric difference.
# returns new frozenset object



