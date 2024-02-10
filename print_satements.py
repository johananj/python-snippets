# Printing
print(var1)
print(var1, var2, var3)
print(str(var1) + str(var2) + str(var3))

print("Value of var1: ", var1)
print("Value of var1: ", var1, "Value of var2: ", var2, "Value of var3: ", var3)

print("Value of var 1, 2 and 3: {} {} {}".format(var1, var2, var3))
print("Value of var 1, 3 and 2: {} {} {}".format(var1, var3, var2))
print("Value of var 1, 3 and 1: {} {} {}".format(var1, var3, var1))

print("Value of var 1, 2 and 3: {v1} {v2} {v3}".format(v1=var1, v2=var2, v3=var3))
print("Value of var 1, 2 and 3: {x1} {x2} {x3}".format(x1=var1, x2=var2, x3=var3))
print("Value of var 1, 2 and 3: {x1} {x2} {x3: .2f}".format(x1=var1, x2=var2, x3=var3))

print("Values: %i, %i, and %0.2f" % (var1,var2,var3))
print("Values: {0}, {1}, and {2: .2f}".format(var1,var2,var3))

# if vars are already defined.
print(f"Values are {var1}, {var2}, and {var3: .2f}")

