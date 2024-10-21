# P3LAB_GoodeTravis
# 2024/10/24
# breaks down a dollar amount into change

#pseudocode
#1 typecast
#2 calc
#3 results - elif

#1
amount = input('Enter the amount of money as a float:$')
value = float(amount)
if value >= 0:
    cents = int(value * 100)
    
#2
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

