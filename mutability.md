| Data Type | Built-in Class | Mutable |
| --------- | --------- | --------- |
| Numbers | int, float, complex | No | 
| Strings | str | No | 
| Tuples | tuple | No | 
| Bytes | bytes | No | 
| Booleans | bool | No | 
| Frozen Sets | frozenset | No | 
| Lists | list | Yes | 
| Dictionaries | dict | Yes | 
| Sets | set | Yes | 
| Byte Arrays | bytearray | Yes | 

# Functions
- Function calls with global variables as argument will lead to mutations (if mutable) of the object referenced by the global variable.
- Functions formal parameter becomes alias of global variable.
- Dont use mutable types as default argument values, and expect those arguments to stay the same everytime they are called, if they are modified within the function.
    + The default value is defined when the interpreter fist parses the function. 
    + Can cause bugs, can also be useful. 