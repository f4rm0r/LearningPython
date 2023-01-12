import turtle
import random
import time

win = turtle.Screen()
win.title("pong by ArchTV")
win.bgcolor ("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle0
paddle_0 = turtle.Turtle()
paddle_0.speed(0)
paddle_0.shape("square")
paddle_0.color("white")
paddle_0.shapesize(stretch_wid=5, stretch_len=1)
paddle_0.penup()
paddle_0.goto(-350, 0)


# Paddle1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 10
ball.dy = 10

# Initialize time 
last_time = time.time()

# points
left_player = 0
Right_player = 0

sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("white")
sketch.penup()
sketch.hideturtle
sketch.goto(0, 260)
sketch.write("Left_player: 0   Right_player: 0", align="center", font=("Courier", 24, "normal"))

# Functions


def paddle_0_up():
    y = paddle_0.ycor()
    y += 20
    paddle_0.sety(y)

def paddle_0_down():
    y = paddle_0.ycor()
    y-= 20
    paddle_0.sety(y)

def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y-= 20
    paddle_1.sety(y)

# Keyboard binding

win.listen()
win.onkeypress(paddle_0_up, "w")
win.onkeypress(paddle_0_down, "s")
win.onkeypress(paddle_1_up, "Up")
win.onkeypress(paddle_1_down, "Down")


# Main game loop

# Random starting direction of ball
direction_set = False

def start_dir():

    global direction_set
    if direction_set == False:
        random_list = [1, -1]

        ball.dx = random.choice(random_list)
        ball.dy = random.choice(random_list)
    direction_set = True

start_dir()

while True:

    win.update()

    # Move the ball

    current_time = time.time()
    dt = current_time - last_time
    last_time = current_time

    speed_scale = dt * 100
    
    ball.setx(ball.xcor() + ball.dx * speed_scale)
    ball.sety(ball.ycor() + ball.dy * speed_scale)

    # Border checking

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        ball.dy *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_0.ycor() + 50 and ball.ycor() > paddle_0.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        ball.dx *= -1

    if paddle_0.ycor() > 250:
        paddle_0.sety(250)
    
    if paddle_0.ycor() < -250:
        paddle_0.sety(-250)
    
    if paddle_1.ycor() > 250:
        paddle_1.sety(250)
    
    if paddle_1.ycor() < -250:
        paddle_1.sety(-250)