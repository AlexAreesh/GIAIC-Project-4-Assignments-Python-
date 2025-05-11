def main():
    # Get the numbers we want to divide
    dividend = int(input("Please enter an integer to be divided: "))  # The number to be divided
    divisor = int(input("Please enter an integer to divide by: "))  # The number we divide by

    # Calculate the quotient and remainder
    quotient = dividend // divisor  # Integer division (quotient)
    remainder = dividend % divisor  # Modulo operation to get the remainder

    # Print the result of division
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
