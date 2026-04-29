while True:
    print(" Driving Age Checker ")
    print("1. Check age")
    print("2. Exit")
    
    choice = input("Pick an option (1-2): ")

    if choice == "1":
        age = int(input("How old are you? "))

        if age >= 18:
            print("You can drive!")
        else:
            wait = 18 - age
            print(f"You have to wait {wait} more years.")
            
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")