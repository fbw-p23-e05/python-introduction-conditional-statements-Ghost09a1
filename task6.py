# input
temperature = float(input("Input the value of temperature you'd like to convert: "))

# F or C?
scale = input("Input the scale shortcut you'd like to convert (F - Fahrenheit, C - Celsius): ")

# c to f/f to c
if scale == 'C':
    fahrenheit = (temperature * 9/5) + 32
    print(f"The temperature in Fahrenheit is {fahrenheit:.2f} degrees.")
elif scale == 'F':
    celsius = (temperature - 32) * 5/9
    print(f"The temperature in Celsius is {celsius:.2f} degrees.")
else:
    print("Invalid scale shortcut. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
