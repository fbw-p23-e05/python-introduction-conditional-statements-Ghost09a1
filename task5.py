# Num
target_number = 7  

# Loop until break
while True:
    guess = int(input("Guess a number between 1 and 10 until you get it right: "))
    
    if guess == target_number:
        print("Well guessed!")
        break
    else:
        print("Try again!")
