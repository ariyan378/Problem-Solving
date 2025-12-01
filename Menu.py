while True:
    # menu
    print("\n1. Cm to Feet")
    print("2. Km to Miles")
    print("3. USD to BDT")
    print("4. Exit")

    # taking choice
    choice = int(input("Enter your choice (1/2/3/4): "))

    if choice == 1:
        cm = float(input("Enter cm: "))
        feet = cm * 0.0328084
        print(f"{cm} cm = {feet:.2f} feet")

    elif choice == 2:
        km = float(input("Enter km: "))
        miles = km * 0.621371
        print(f"{km} km = {miles:.2f} miles")

    elif choice == 3:
        USD = float(input("Enter USD: "))
        BDT = USD * 122
        print(f"{USD} USD = {BDT:.2f} BDT")

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please enter 1-4.")
