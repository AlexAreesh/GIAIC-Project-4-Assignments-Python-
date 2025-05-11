# ## Problem Statement

# 10 even
# 11 odd
# 12 even
# 13 odd
# 14 even
# 15 odd
# 16 even
# 17 odd
# 18 even
# 19 odd

# ## Starter Code

# ```bash
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
# ```

## Solution By GIT

def main():
    for i in range(10):
        if is_odd(i):
            print('odd')
        else:
            print('even')
            
def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns true.
    """
    
    remainder = value % 2  # 0 if value is divisible by 2, 1 if it isn't
    return remainder == 1


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()

#Imporvised Solution

# Your logic is almost there, but you're printing just "even" or "odd" — 
# whereas the problem requires both the number and its label.

def main():
    for i in range(10, 20):  # Loop from 10 to 19 inclusive
        if is_odd(i):
            print(f"{i} odd")
        else:
            print(f"{i} even")

def is_odd(value: int):
    """
    Returns True if value is odd, otherwise False.
    """
    return value % 2 == 1  # Odd numbers give remainder 1 when divided by 2

# Required line to call main()
if __name__ == '__main__':
    main()
