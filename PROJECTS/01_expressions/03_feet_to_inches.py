"""
An example program with constants
"""

INCHES_IN_FOOT = 12  # Conversion factor. There are 12 inches for 1 foot.

def main():
    feet = float(input("Enter number of feet: "))  # Get the number of feet, make sure to cast it to a float!
    inches = feet * INCHES_IN_FOOT  # Perform the conversion
    print("That is", inches, "inches!")  # Output the result
    
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
