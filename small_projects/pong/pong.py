import turtle
import random

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
ball.dx = 0.04
ball.dy = 0.04

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
def start_dir():

    random_list = ["left", "right"]

    left = ball.dx = 0.04
    right = ball.dx = -0.04
    start_dir = random.choice(random_list)

    if start_dir == left:
        left
    if start_dir == right:
        right

while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

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
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_0.ycor() + 50 and ball.ycor() > paddle_0.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1

    if paddle_0.ycor() > 250:
        paddle_0.sety(250)
    
    if paddle_0.ycor() < -250:
        paddle_0.sety(-250)
    
    if paddle_1.ycor() > 250:
        paddle_1.sety(250)
    
    if paddle_1.ycor() < -250:
        paddle_1.sety(-250)