"""
Program: add2numbers
--------------------
This program asks the user for two integers and prints their sum.
"""

def main():
    print("This program adds two numbers.")
    
    # Take first input
    num1 = int(input("Enter first number: "))
    
    # Take second input
    num2 = int(input("Enter second number: "))
    
    # Calculate sum
    total = num1 + num2
    
    # Display the result
    print("The total is " + str(total) + ".")

# This provided line is required at the end of Python file
if __name__ == '__main__':
    main()
