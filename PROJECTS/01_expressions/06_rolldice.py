"""
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""

# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES = 6

def main():
    # Roll die
    die1 = random.randint(1, NUM_SIDES)  # Roll for the first die
    die2 = random.randint(1, NUM_SIDES)  # Roll for the second die
    
    # Get their total
    total = die1 + die2
    
    # Print out the results
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
