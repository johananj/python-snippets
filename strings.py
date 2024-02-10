# Strings are immutable. They cannot be changed in-place. 
# Convert to a list to make them mutable. 
# Look at lists.py
# String methods return a new string. list methods do it in place.

# Loop through a string
for a_char in a_str:
    print(a_char)
    

# the string module provides a list of alphabets, usage:
string.ascii_letters
# convert it to a list using
list(string.ascii_letters)
# other attributes
ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
hexdigits = '0123456789abcdefABCDEF'
octdigits = '01234567'
printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
whitespace = ' \t\n\r\x0b\x0c'

# Classifying a character or string
s.isalnum()
s.isalpha()
s.isdigit()
s.isidentifier()
s.islower()
s.isprintable()
s.isspace()
s.istitle()
s.isupper()

# Splitting
# split from left
s.split('.',maxsplit=1) 
# split from right
s.rsplit('.',maxsplit=1)
# split lines based on many kinds of line separators like return character
s.splitlines()
# to keep the ends
s.splitlines(True) 

# String building
# use join to build a string from a list
# with a specified separator
a_list = ['h', 'e', 'l', 'l', 'o']
"".join(a_list) # returns "hello"
# use string concatenation
for i in range(len(a_list)):
    mystring += a_list[i]
# use StringIO
mystr = StringIO()
for i in range(len(a_list)):
    mystr.write(a_list[i])
mystr.getvalue() # returns "hello"


# Finding substrings
s = "foobar"
# True
s.endswith("bar")
s.startswith("foo")
# find index
s.find("fo") #returns 0, the index

# Conversions: integer and character
# converting int to char
chr(65)
# converting char to int
ord('A')
# int of 0, A and a are 48, 65, 97

# Comparing strings, the following are True
"Abc" <= "abc"
"Abc" == "Abc"
"Abc" != "ABC"

# compare if both refer to the same object.
str_1 = "Abc"
str_2 = "Abc"
str_3 = str_2
# the following are all true
str_1 is str_2
str_1 is str_3
str_3 is str_2

# Counting characters in a string.
from collections import Counter
a_str = 'abcde'
a_cnt = Counter(a)
# Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1})
