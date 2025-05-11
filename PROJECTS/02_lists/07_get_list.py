# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.
# Here's a sample run (user input is in blue):
# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']


def main():
    lst = []  # Create an empty list to store the values

    while True:
        val = input("Enter a value: ")  # Ask for input
        if val == "":  # Check if input is empty (user just pressed Enter)
            break
        lst.append(val)  # Add the non-empty input to the list

    print("Here's the list:", lst)


# This provided line is required to call the main() function.
if __name__ == '__main__':
    main()






