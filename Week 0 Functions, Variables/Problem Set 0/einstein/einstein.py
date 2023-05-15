def emc2(mass: str):
    """Convert mass in kg to energy in J, and print result."""
    c = 300000000
    energy = int(mass)*c**2
    print(f"E: {energy}")

emc2(input("m: "))