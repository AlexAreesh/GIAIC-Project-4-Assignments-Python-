low = 1
high = 10

print("Think of a number from 1 to 10.")
input("Press Enter when ready...")

while True:
    guess = (low + high) // 2
    print("I guess:", guess)
    feedback = input("Is it (h)igh, (l)ow, or (c)orrect? ").lower()

    if feedback == 'h':
        high = guess - 1
    elif feedback == 'l':
        low = guess + 1
    elif feedback == 'c':
        print("Yay! I guessed it.")
        break