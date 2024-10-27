 # Travis Goode
 # 10/27/2024
 # P4LAB1A
 # Turtle grapics
import turtle          
win = turtle.Screen()  
t = turtle.Turtle()


#1 display option
#2 loop the staetement
#3 gather user input
#4 draw requested shape /w tuple incase caps button broken

# 1
t.pensize(4)            # increase pensize (takes integer)
t.pencolor("red")     # set pencolor (takes string)
t.shape("turtle")

# 2
while True:
    #3
    numSides = input("Triangle or Square: ") 

# 4
    if numSides in ("Square", "square"):
        for _ in range(4):
            t.forward(80)  
            t.right(90)     

    if numSides in ("Triangle", "triangle"):
        for _ in range(3):
            t.forward(80)  
            t.left(120)     
