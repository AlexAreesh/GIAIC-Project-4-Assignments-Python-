def get_last_element(lst):
    """
    Prints the last element of the provided list.
    """
    print(lst[-1])

# No need to edit the code beyond this point

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()  # Get the list of elements from the user
    get_last_element(lst)  # Print the last element of the list

if __name__ == '__main__':
    main()
