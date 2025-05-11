import random

num = random.randint(1,10)
print("Guess the number from 1 to 10")

while True:
    guess = int(input("Your guess: "))
    if guess == num:
        print("Correct!")
        break
    else:
        print("Wrong, try again.")
