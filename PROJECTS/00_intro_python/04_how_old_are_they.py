def main():
    anton: int = 21  # Anton's age
    beth: int = anton + 6  # Beth is 6 years older than Anton
    chen: int = beth + 20  # Chen is 20 years older than Beth
    drew: int = chen + anton  # Drew is Chen's age + Anton's age
    ethan: int = chen  # Ethan is the same age as Chen

    # Print their names and ages exactly as required
    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))

# Required to call the main() function
if __name__ == '__main__':
    main()
