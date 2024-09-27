# Travis Goode
# 9/27/24
# P1HW1
# Basic calculator 

# exponets 
def calculate_exponent(base, exponent):
    return base ** exponent

# order of opperations
def calculate_expression(num1, num2, num3):
    return (num1 + num2) - num3

# exe
def main():
    
    print("\n")
    print("-----Calculating Exponents-----")
    print("\n")
    
    
    base = int(input("Enter an integer as the base value: "))
    exponent = int(input("Enter an integer as the exponent: "))
    print("\n")  
    
    
    result = calculate_exponent(base, exponent)
    
    
    print(f"{base} raised to the power of {exponent} is {result} !!")

    # sorry if this is a bad way to do line spacing
    print("\n")
    print("-----Addition and Subtraction-----")
    print("\n")
    
    # add/sub script
    num1 = int(input("Enter a starting integer: "))
    num2 = int(input("Enter an integer to add: "))
    num3 = int(input("Enter an integer to subtract: "))
    print("\n")  # Double space after entering the integer to subtract
    
    
    final_result = calculate_expression(num1, num2, num3)
    
    
    print(f"{num1} + {num2} - {num3} is equal to {final_result}.")

# Run function
if __name__ == "__main__":
    main()
