import turtle
import random
turtle.colormode(255)
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
list=[]
def bal():
 balloon=turtle.Turtle()
 balloon.speed(0)
 balloon.hideturtle()
 balloon.shape("circle")
 balloon.color(random.randint(1,255),random.randint(1,255),random.randint(1,255))
 balloon.up()
 balloon.left(90)
 balloon.goto(random.randint(-250,250),250)
 balloon.showturtle()
 list.append(balloon) 
while True:
   t=random.randint(1,25)
   if t==9:
    bal()
   for balloon in list:
    balloon.backward(5)
    if balloon.distance (food)<15:
     list.remove(balloon)
     balloon.hideturtle()
    elif balloon.ycor()<-250:
     balloon.hideturtle()
     list.remove(balloon)
