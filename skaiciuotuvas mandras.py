while True:
    print("""
    Welcome to calculator v0.0.1
    Commands:
          + | add two numbers
          - | subtract two numbers
          * | multiply two numbers
          / | divide two numbers
          exit 
    """)
    command = input("Enter command: ")
    if command == "exit":
        print("Goodbye :)")
        break

    elif command == "+":
        num_1 = float(input("Enter number1: "))
        num_2 = float(input("Enter number2: "))
        print("result is ", num_1 + num_2)

    elif command == "-":
        num_1 = float(input("Enter number1: "))
        num_2 = float(input("Enter number2: "))
        print("result is ", num_1 - num_2)
    
    elif command == "*":
        num_1 = float(input("Enter number1: "))
        num_2 = float(input("Enter number2: "))
        print("result is ", num_1 * num_2)

    elif command == "-":
        num_1 = float(input("Enter number1: "))
        num_2 = float(input("Enter number2: "))
        print("result is ", num_1 / num_2)

    else:
        print("Invalid command :(")