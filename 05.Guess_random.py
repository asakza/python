# generate a random number, input 3 guess, if right guess, print you won if guess wrong print try again

print("Please enter any Number Within range of 1 - 10")
print("You will be provided with a maximumm of 3 chances")
print("All the Best !!!!!!!")

import random
guess_number = random.randint(1,10)
print(guess_number)
chances_available = 3

for chance in range(chances_available):
    guess = int(input("Enter your Guess"))
    if guess == guess_number:
        print("You Won") 
        break
    else:
        if chance == chances_available - 1:
            print("Better Luck next time")