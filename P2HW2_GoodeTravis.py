# Travis Goode
# 10/13/2024
# P2HW2
# collects grades to find various vales

#Pseudocode
#1 collect grades
#2 Calculate the statistics
#3 Display the results

#1 
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))
print()

#2 Calculate the statistics
lowest_grade = min(grade1, grade2, grade3, grade4, grade5, grade6)
highest_grade = max(grade1, grade2, grade3, grade4, grade5, grade6)
total_sum = grade1 + grade2 + grade3 + grade4 + grade5 + grade6
average_grade = total_sum / 6

print("------------Results------------")

#3
print(f"Lowest Grade: {lowest_grade:>11.2f}")
print(f"Highest Grade: {highest_grade:>10.2f}")
print(f"Sum of Grades: {total_sum:>11.2f}")
print(f"Average: {average_grade:>16.2f}")
print("----------------------------------------")
