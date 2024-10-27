 # Travis Goode
 # 10/27/2024
 # P4LAB1B
 # Turtle grapics
import turtle          
win = turtle.Screen()  
t = turtle.Turtle()


#1 display option
#2 square
#3 reposition
#4 triangle

# 1
t.pensize(4)        
t.pencolor("red")     
t.shape("turtle")

#T
t.forward(200)
t.right(180)
t.forward(100)
t.left(90)
t.forward(200)
#reposition    
t.penup()
t.left(90)
t.forward(150)
t.pendown()
#G
for _ in range(3):
    t.left(30)
    t.forward(15)
t.left(90)
t.forward(25)
t.penup()
t.right(90)
t.forward(25)
t.pendown()
for _ in range(9):
    t.left(30)
    t.forward(25)
t.forward(35)
