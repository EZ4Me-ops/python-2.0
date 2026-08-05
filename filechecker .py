def  read_file():
    while True:
        filename = input("Enter the name of the file to read (or 'exit' to quit): ")
        
        if filename.lower() == 'exit':
            print("Exiting the program.")
            break
        
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print("\nFile contents:\n")
                print(content)
                break  
        
        except FileNotFoundError:
            print("File not found. Please try again or type 'exit' to quit.")

read_file()