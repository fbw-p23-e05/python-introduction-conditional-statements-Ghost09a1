# one line of code
upper_part = '\n'.join(['* ' * i for i in range(1, 6)])

# Lower part 
lower_part = '\n'.join(['* ' * i for i in range(4, 0, -1)])

# Combine and print 
pattern = upper_part + '\n' + lower_part
print(pattern)