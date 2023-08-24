# Input
first_number = int(input("First number: "))
second_number = int(input("Second number: "))
third_number = int(input("Third number: "))

# sum o num
sum_of_numbers = first_number + second_number + third_number

# equal else triple
if first_number == second_number == third_number:
    triple_sum = 3 * sum_of_numbers
    print("The triple sum is:", triple_sum)
else:
    print("The sum is:", sum_of_numbers)