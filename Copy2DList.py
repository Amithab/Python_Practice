import copy

# Create a 2d list
a = [ [ 1, 2, 3 ] , [ 4, 5, 6 ] ]

# Try to copy it
b = copy.copy(a) # Error:  creates shallow copy

# At first, things seem ok
print("At first...")
print("   a =", a)
print("   b =", b)

# Now modify a[0][0]
a[0][0] = 9
print("But after a[0][0] = 9")
print("   a =", a)
print("   b =", b)
