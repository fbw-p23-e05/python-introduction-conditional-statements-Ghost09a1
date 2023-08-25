# input
first_number = int(input("First number: "))
second_number = int(input("Second number: "))

# difference 
difference = abs(first_number - second_number)

# Check & print
if first_number > second_number:
    double_difference = 2 * difference
    print("The result of calculation is", double_difference)
else:
    print("The result of calculation is", difference)