C = 299792458  # The speed of light in m/s

def main():
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    # Calculate energy using the mass-energy equivalence formula
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Display the results to the user
    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    print(str(energy_in_joules) + " joules of energy!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
