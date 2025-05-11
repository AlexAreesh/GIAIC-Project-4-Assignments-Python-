word = "banana"
guesses = []
tries = 6



# not working fine



print("Welcome to Hangman!")

while tries > 0:
    display = ""
    for char in word:
        if char in guesses:
            display += char
        else:
            display += "_"

    print("Word:", display)

    # Check for win condition here, after showing current state
    if "_" not in display:
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in word and guess not in guesses:
        guesses.append(guess)
    elif guess in guesses:
        print("You've already guessed that letter!")
    else:
        tries -= 1
        print(f"Wrong guess! Tries left: {tries}")

if tries == 0:
    print(f"You lost! The word was: {word}")
