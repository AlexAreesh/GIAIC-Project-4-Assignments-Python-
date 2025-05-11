import math  # Import the math library so we can use the sqrt function

def main():
    # Get the two side lengths from the user and cast them to be numbers
    ab = float(input("Enter the length of AB: "))  # Side AB (one of the perpendicular sides)
    ac = float(input("Enter the length of AC: "))  # Side AC (the other perpendicular side)

    # Calculate the hypotenuse using the two sides and print it out
    bc = math.sqrt(ab**2 + ac**2)  # Using Pythagorean theorem to calculate BC (hypotenuse)
    print(f"The length of BC (the hypotenuse) is: {bc}")  # Output the result


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
