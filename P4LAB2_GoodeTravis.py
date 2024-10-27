 # Travis Goode
 # 10/27/2024
 # P4LAB2
 # Multiplication Tables
while True:
    user_input = int(input("Enter an integer: "))
    print("")
        
    if user_input < 0:
        print("This program does not handle negative number")
    else:
        for i in range(1, 13):
            print(f"{user_input} x {i} = {user_input * i}")
    print("")

    run_again = input("Would you like to run the program again?: ")
    print("")
    if run_again != "yes":
        print("Exiting program...")
        break
