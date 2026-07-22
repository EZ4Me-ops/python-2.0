def km_to_m(km):
    return km * 1000

def m_to_cm(m):
    return m * 100

def cm_to_mm(cm):
    return cm * 10


while True:
    print("\n1. km → m | 2. m → cm | 3. cm → mm | 4. Exit")
    choice = input("Choice: ")

    if choice == "4":
        break

    if choice in ("1", "2", "3"):
        val = float(input("Enter value: "))

        if choice == "1":
            print(f"Result: {km_to_m(val)} m")
        elif choice == "2":
            print(f"Result: {m_to_cm(val)} cm")
        elif choice == "3":
            print(f"Result: {cm_to_mm(val)} mm")
    else:
        print("Invalid choice!")