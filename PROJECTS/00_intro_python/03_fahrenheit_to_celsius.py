def main():
    # Prompt the user for temperature in Fahrenheit
    fahrenheit = input("Enter temperature in Fahrenheit: ")
    
    # Convert the input to a float
    fahrenheit = float(fahrenheit)
    
    # Calculate Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    
    # Display the result
    print("Temperature: " + str(fahrenheit) + "F = " + str(celsius) + "C")

# This provided line is required at the end of Python file
if __name__ == '__main__':
    main()
