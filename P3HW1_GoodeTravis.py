#P3HW1_GoodeTravis 
#I did put a comment here
#2024/10/20
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))
print('')
# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

print('------------Results------------')

low = min(grades)
high = max(grades)
sum = sum(grades)
avg = sum / 6

print(f"Lowest Grade: {low:>11.2f}")
print(f"Highest Grade: {high:>10.2f}")
print(f"Sum of Grades: {sum:>11.2f}")
print(f"Average: {avg:>16.2f}")

print("----------------------------------------")

# determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
else:
    if avg >= 80:
        print('Your grade is: B')
    else:
        if avg >= 70:
            print('Your grade is: c')
        else:
            if avg <= 60:
                print('Your grade is: F') # TO DO: finish this





