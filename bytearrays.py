# Stores binary data. 
# Using ASCII is direct (i.e upto 127)
# Use escape sequence for unicode. 
# Use bytearray constructor to create. 
# Bytes - Immutable. ByteArray - Mutable.
# Accepts only 0 to 255

# Create ASCII String
bytearray(b"Hello World")
# Other ways to create?

# Modifying. Needs integer. Not Str. Not bytes. 
bytearray[1] = 69 # "HEllo World"
bytearray[2] = "L" # TypeError
bytearray[2] = b"L" # TypeError
bytearray[2] = bytearray(b"L") # TypeError
bytearray[2] = ord("L") # Works. "HELlo World"
bytearray[2] = 600 # Value error. Should be in (0,256)
