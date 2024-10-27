# Travis Goode
# 10/23/2024
# P3HW2
# calculates pay & overtime if nessecary.


#1 define var
#2 user input
#3 elif
#4 do math
#5 display results


#1
RegHour = 40
ExtraPay = 26.25

#2
Name = input("Enter employee's name: ")
WorkHours = float(input("Enter number of hours worked: "))
Pay = float(input("Enter employee's pay rate: "))


print("-------------------------------------")
print(f" Employee name:{Name} ")
print("")

#3
if WorkHours > RegHour:
    OverTime = WorkHours - RegHour
    WorkHours = RegHour
else:
    OverTime = 0
    

#4    
RegHour_Pay = WorkHours * Pay
RegPay = WorkHours * Pay
OverPay = OverTime * ExtraPay
Gross = RegPay + OverPay

#5
print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
print("--------------------------------------------------------------------------------------")
print(f"{WorkHours + OverTime:<15}{Pay:<15}{OverTime:<15}{OverPay:<15}{RegHour_Pay:<15}{Gross:<15}")


