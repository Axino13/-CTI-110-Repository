#Travis Goode
#11/24/2024
#P5HM
#Addtion and subtraction quiz using randomly generated numbers


#1. import
#2. addition
#3. subtraction
#4. guessing
#5. main menu
#6. start

#1
import random


#2
def addition():
    num1= random.randint(1,100)
    num2 = random.randint(1, 100)
    answer = num1 + num2
    print(f"  {num1}")
    print(f"+ {num2}\n")
    guessing(answer)


#3
def subtraction():
    num1= random.randint(1,100)
    num2 = random.randint(1, 100)
    answer = num1 - num2
    print(f"  {num1}") 
    print(f"- {num2}\n")
    guessing(answer)



#4
def guessing(answer):
    guesses = 0
    while True:
        user_answer = int(input("Enter answer.\n"))
        guesses += 1

        if user_answer == answer:
                print(f"Congratulations!!!! Your answer is correct.")
                print(f"Number of gueses: {guesses}\n")
                break

        while user_answer != answer:
            if user_answer < answer:
                print("Sorry, guess is too low.\n")
            if user_answer > answer:
                print("Sorry, guess is too high.\n")

            user_answer = int(input("Try again : "))
            guesses += 1

            if user_answer == answer:
                print(f"Congratulations!!!! Your answer is correct.")
                print(f"Number of guesses: {guesses}\n")
                main_menu()
                break


#5
def main_menu():
    while True:
        print("MAIN MENU")
        print("--------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit\n")


        pick = input("Please choose one of the menu options: ")

        if pick.isdigit():
            pick = int(pick)
            if pick == 1:
                addition()
            elif pick == 2:
                subtraction()
            elif pick == 3:
                print("Thank you for playing...")
                print("Bye!!")
                break
            else:
                print("Invalid only choose 1, 2, or 3") 



#6
def start_quiz():
    print("Welcome to Math Quiz")      
    print("")
    print("")
    main_menu()


start_quiz()
    
