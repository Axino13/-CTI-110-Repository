# P5LAB_GoodeTravis
# 2024/11/16
# simulated checkout machine, input a value and displays change breakdown if needed

#pseudocode
#1 Import
#2 func - disperse
#3 elif
#4 __main__


#1
import random


#2
def disperse_change(change):
    cents = int(round(change * 100))

    Dollars = cents // 100
    cents %= 100
    Quarters = cents // 25
    cents %= 25
    Dimes = cents // 10
    cents %= 10
    Nickels = cents // 5
    cents %= 5
    Pennies = cents
    
# 
    if any([Dollars, Quarters,Dimes, Nickels, Pennies]):
        if Dollars > 0:
            print(f"{Dollars} Dollar{'s' if Dollars > 1 else ''}")
        if Quarters > 0:
            print(f"{Quarters} Quarter{'s' if Quarters > 1 else ''}")
        if Dimes > 0:
            print(f"{Dimes} Dime{'s' if Dimes > 1 else ''}")
        if Nickels > 0:
            print(f"{Nickels} Nickel{'s' if Nickels > 1 else ''}")
        if Pennies > 0:
            print(f"{Pennies} Pennie{'s' if Pennies > 1 else 'y'}")

    else:
        print('No Change')

#4
def main():
    owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${owed}")
    pay = float(input("How much cash will you put in the self-checkout? "))

    if pay >= owed:
        change = pay - owed
        print(f"Change is: ${change:.2f}")
        disperse_change(change)
    else:
        change = owed - pay
        print(f"Change owed is: ${change:.2f}")
        
        

if __name__ == "__main__":
    main()
