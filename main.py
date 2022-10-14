from turtle import *
from random import *
from time import *

setup(440,600)
title("Flora's Pong Game")

class factor(Turtle):
    def __init__(self, shape:str, size, pos, color="black"):
        super().__init__(shape=shape)
        self.penup()
        self.shape(shape)
        self.color(color)
        self.shapesize(*size)
        self.setpos(pos)

player = factor("square", (1,4), (0,-150))

ball = factor("circle", (1,1), (0,200), "Purple")

def left():
    if player.xcor() != -220: 
        player.bk(10)

def right():
    if player.xcor() != 220:
        player.fd(10)

onkey(left,"Left")
onkey(right,"Right")

listen()

def ballMoving(ballXSpeed,ballYSpeed):

    ball.goto(ball.xcor()+ballXSpeed, ball.ycor()+ballYSpeed)
    
    ballX = ball.xcor()
    ballY = ball.ycor()

    if ballX > 220 or ballX < -220:
        ballXSpeed *= -1

    if ballY > 300:
        ballYSpeed *= -1
    elif ballY < -300:
        return

    if player.distance(ball) <= 30:
        ballYSpeed *= -1

    ontimer(ballMoving(ballXSpeed,ballYSpeed), 200)

ballMoving(5,5)

done()
