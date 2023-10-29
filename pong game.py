import turtle

window = turtle.Screen() #creates a pop up window
window.title("Pong by @RaiBread") #title of window
window.bgcolor("black") #changing background color of window
window.setup(width = 800, height = 600) #changing size of window to 800 x 600 pixels
window.tracer(0) #stops window from updating which allows us to speed up our games

# Score
score_a = 0 # start game at zero
score_b = 0 

# Paddle A
paddle_a = turtle.Turtle() #turtle.Turtle is known as a "turtle object"
paddle_a.speed(0) # setting speed of animation to maximum possible speed, need to do it for turtle.
paddle_a.shape("square") # we are giving the paddle a shape. turtle has a few built-in shapes
paddle_a.color("white") # setting color of paddles
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1) #stretches shape so it turns into a rectangle
paddle_a.penup() # turtles by definition draw a line, this erases that line
paddle_a.goto(-350, 0) # setting a spot for the paddle to be on the screen (think of screen like an axis)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0) #moving to right side of screen

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0) #moving to right side of screen
ball.dx = 2 # d means delta (change). speed of x movement. we want it to go up two (y-axis) and to the right two (x-axis)
ball.dy = -2 # speed of y movement. every time the ball moves, it moves by 2 pixels

# Creating a "Pen" from turtle module to create a score
pen = turtle.Turtle()
pen.speed(0) # animation speed
pen.color("white")
pen.penup() # we don't want to draw a line when pen moves
pen.hideturtle() # we don't want to see pen, just the text it will write
pen.goto(0, 260) # where to place pen
pen.write('''Player A: 0  Player B: 0''', align = "center", font = ("Courier", 24, "normal")) # default score on screen

# Functions (We want to move paddle a and b up and down)
def paddle_a_up(): 
    y = paddle_a.ycor() # finding the y coordinate
    y += 20 # to move paddle up, need to make the y coordinate higher. adds 20 pixels to y coordinate
    paddle_a.sety(y) # setting y to the new y

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up(): 
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding, calling the above functions
window.listen() # tells it to listen for keyboard input - part of turtle module
window.onkeypress(paddle_a_up, "w") # when user presses w, call function paddle_a_up and move that paddle upwards
window.onkeypress(paddle_a_down, "s") # when user presses s, call paddle_a_down and move paddle down
window.onkeypress(paddle_b_up, "Up") # up arrow
window.onkeypress(paddle_b_down, "Down") # down arrow

# Every game needs a Main Game Loop
while True: #while loop
    window.update() # every time the loop runs, it updates the screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx) # ball starts at x = 0 First time through loop it will go x = 2 and so on 
    ball.sety(ball.ycor() + ball.dy) # ball starts at y = 0 First time through loop it will go y = 2 and so on 

    # Border checking (what do we want to happen when the ball hits the border?)
    # height of window is 600, so top of window is y = 300 and bottom is y = -300
    # ball is 20 high by 20 wide
    if ball.ycor() > 290: # if ball gets above 290 and hits top
        ball.sety(290) # set ball back to 290
        ball.dy *= -1 # reverses direction of dy so it goes in other direction when it hits

    elif ball.ycor() < -285: # if ball hits bottom
        ball.sety(-285) # set ball back to -285
        ball.dy *= -1 # change direction
    
    if ball.xcor() > 390: # if ball goes past the paddles and hits the right side
        ball.goto(0, 0) 
        ball.dx *= -1
        score_a += 1 # Player A gets a point if ball goes off right side of screen
        pen.clear() #clear what was previously on screen
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))
    
    elif ball.xcor() < -390: # if ball passes paddle on left side
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1 # Player B gets a point if ball goes off left side of screen
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))

    # Paddle and ball collisions so the ball reverses direction when hits paddle
    if (ball.xcor() > 340 and ball.xcor() < 345) and (ball.ycor() < paddle_b.ycor() + 55 and ball.ycor() > paddle_b.ycor() - 55):
        # if ball is between the edges of the paddle (> 340) and between the top of the paddle and the bottom of the paddle
        ball.setx(340) 
        ball.dx *= -1 

    # Paddle A
    elif (ball.xcor() < -340 and ball.xcor() > -345) and (ball.ycor() < paddle_a.ycor() + 55 and ball.ycor() > paddle_a.ycor() - 55):
        ball.setx(-340) 
        ball.dx *= -1 

window.mainloop()