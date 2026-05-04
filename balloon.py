import turtle
import random
screen=turtle.Screen()
food=turtle.Turtle()
food.shape("triangle")
food.up()
food.goto(-200,-200)
food.left(90)
def right():
    x=food.xcor()+10
    y=food.ycor()
    food.goto(x,y)
screen.listen()
screen.onkey(right,"Right")
def left():
    x=food.xcor()-10
    y=food.ycor()
    food.goto(x,y)
screen.onkey(left,"Left")
balloon=turtle.Turtle()
balloon.shape("circle")
balloon.up()
balloon.left(90)
balloon.goto(random.randint(-250,250),250)
while True:
 balloon.backward(250)

