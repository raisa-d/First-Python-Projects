import turtle as t
from random import random

t.width(3)
t.color("red")
t.penup() # lift pen up
t.setpos(-325, -10)
t.left(180)
t.pendown()

# writing the "R"
t.right(90)
t.forward(100)
t.right(30) 
# the curve in the R
t.circle(-30, 300, 10)
# line in R
t.right(170)
t.forward(90)

# making a space between the R and the A
t.color("orange")
t.penup()
t.home()
t.setpos(-250, -10)
t.pendown()

# writing the "A"
# sides of A
t.left(80)
t.forward(100)
t.right(160)
t.forward(100)

# move pen to start of crossing the A
t.penup()
t.right(100)
t.forward(35)
t.right(100)
t.forward(50)
t.pendown()

# making cross of the A
t.right(80)
t.forward(18)

# making space between A and I
t.color("yellow")
t.penup()
t.right(90)
t.forward(50)
t.left(90)
t.forward(30)
t.pendown()

# writing the I
t.forward(50)
t.right(180)
t.forward(25)
t.right(90)
t.forward(100)
t.left(90)
t.forward(25)
t.right(180)
t.forward(50)

# moving turtle to S
t.penup()
t.color("green")
t.goto(-120, -5)
t.right(30)
t.pendown()

# writing S
t.circle(25, 200, 15)
t.forward(10)
t.right(30)
t.circle(-25, 160, 15)

# move pen to write A
t.color("cyan")
t.penup()
t.goto(-50, -10)
t.left(90)
t.pendown()

# writing A
t.left(10)
t.forward(100)
t.right(160)
t.forward(100)

# move pen to start of crossing the A
t.penup()
t.right(100)
t.forward(35)
t.right(100)
t.forward(50)
t.pendown()

# making cross of the A
t.right(80)
t.forward(18)

# making X axis
t.color("purple")
t.penup()
t.goto(-360, -10)
t.pendown()
t.forward(720)

# making Y axis
t.penup()
t.goto(0, -325)
t.left(90)
t.pendown()
t.forward(660)

t.mainloop() # so that window doesn't close until we hit close